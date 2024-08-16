import click
from todoist_api_python.api import TodoistAPI
from todoist.config import Config
from todoist.constants import LIST_HELP
from todoist.utils import view_inbox
from todoist.domain import Task
from rich.console import Console
from typing import Iterable

console = Console()


class AliasedGroup(click.Group):
    def get_command(self, ctx, cmd_name):
        try:
            cmd_name = ALIASES[cmd_name].name
        except KeyError:
            pass
        return super().get_command(ctx, cmd_name)  # type: ignore


@click.group(cls=AliasedGroup)
@click.pass_context
def entry_point(context):
    # todoist  # TODO: alias this in pyproject.toml as td after uninstalling todo-cli
    config = Config()
    api = TodoistAPI(token=config.TODOIST_API_KEY)  # type: ignore
    context.obj = {"api": api}


@entry_point.command(
    name="list",
    help=LIST_HELP,
    context_settings={"ignore_unknown_options": True},
)
@click.argument("args", nargs=-1)
@click.pass_context
def list_cli(context, args: Iterable):
    api = context.obj["api"]
    tasks = [Task.from_dict(_.to_dict()) for _ in api.get_tasks()]
    for arg in args:
        if len(arg) > 2 and arg[:2] == "-@":
            tasks = [_ for _ in tasks if arg[2:] not in _.labels_str]
        if arg[0] == "@":
            tasks = [_ for _ in tasks if arg[1:] in _.labels_str]
    view_inbox(tasks)


ALIASES = {
    "ls": list_cli,
}
