import pytest
from todoist.constants import TODAY, TOMORROW
from todoist.domain import Task
from todoist_api_python.models import Due
from datetime import date, datetime, time


@pytest.fixture
def task_factory():
    def __func(id: int, content: str = "", due_datetime: str = "") -> Task:
        due = (
            Due(datetime=due_datetime, is_recurring=False, string="", date=due_datetime)
            if due_datetime
            else ""
        )
        data = {
            "id": id,
            "content": content,
            "assignee_id": "",
            "assigner_id": "",
            "comment_count": "",
            "is_completed": "",
            "created_at": "",
            "creator_id": "",
            "description": "",
            "due": due,
            "labels": "",
            "order": "",
            "parent_id": "",
            "priority": "",
            "project_id": "",
            "section_id": "",
            "url": "",
            "duration": "",
        }
        return Task(**data)

    return __func


def test_sorted_will_order_tasks_by_id_ascending(task_factory):
    todo_1 = task_factory(id=1)
    todo_2 = task_factory(id=2)
    todo_3 = task_factory(id=3)

    todos = [todo_3, todo_1, todo_2]

    expected = [todo_1, todo_2, todo_3]
    assert expected == sorted(todos)


def test_sorted_will_order_tasks_by_datetime_asc_nulls_last(task_factory):
    todo_1 = task_factory(id=1)
    todo_2 = task_factory(id=2, due_datetime=TOMORROW.isoformat())
    todo_3 = task_factory(id=3, due_datetime=TODAY.isoformat())
    todo_4 = task_factory(
        id=4, due_datetime=datetime.combine(TODAY, time(hour=9, minute=30)).isoformat()
    )

    todos = [_.id for _ in sorted([todo_1, todo_2, todo_3, todo_4])]

    expected = [_.id for _ in [todo_4, todo_3, todo_2, todo_1]]
    assert expected == todos
