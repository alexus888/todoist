from typing import List, Optional
from collections import defaultdict
from todoist.domain import Task
from todoist.constants import TODAY, TOMORROW
from datetime import datetime
from rich.console import Console


console = Console()


def parse_integer(input: str) -> Optional[int]:
    try:
        return int(input)
    except ValueError:
        return None


def view_inbox(tasks: List[Task]):
    tasks = [Task.from_dict(_.to_dict()) for _ in tasks]

    buckets = defaultdict(list)

    for task in sorted(tasks):
        if not task.due:  # NOTE: this is the "Non-urgent" bucket
            buckets[""].append(task)
        else:
            buckets[datetime.strptime(task.due.date, "%Y-%m-%d").date()].append(task)

    prefixes = {TODAY: "Today", TOMORROW: "Tomorrow"}
    print()
    for key, tasks in buckets.items():
        if key == "":
            header = "Non-urgent"
        elif key < TODAY:
            day = key.strftime("%a %b %d, %Y")
            header = day + " - [bold white]Overdue[/bold white]"
        else:
            day = key.strftime("%a %b %d, %Y")
            prefix = prefixes.get(key, "")
            header = f'{day}[bold white]{" - " + prefix if prefix else ""}[/bold white]'
        formatted_header = (
            f"[bold medium_spring_green]{header}[/bold medium_spring_green]"
        )
        console.print(formatted_header)
        for task in tasks:
            labels = " ".join("@" + _ for _ in task.labels)
            if task.due:
                string = task.due.string if task.due.is_recurring else ""
                due = day + " " + string
            else:
                due = ""
            print(f"\t{task.content} {due} {labels}")
        print()
