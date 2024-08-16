from todoist_api_python.models import Task as BaseTask, Due
from datetime import datetime
import pytz


target_timezone = pytz.timezone("America/Chicago")


def convert_to_timezone(due: Due, target_timezone=target_timezone) -> str:
    if not due:
        return ""

    if due.datetime and due.datetime.endswith("Z"):
        result = datetime.strptime(due.datetime, "%Y-%m-%dT%H:%M:%SZ")
        return pytz.utc.localize(result).isoformat()
    elif due.datetime and "T" in due.datetime:
        result = datetime.strptime(due.datetime, "%Y-%m-%dT%H:%M:%S")
        return pytz.utc.localize(result).isoformat()
    else:
        result = datetime.strptime(due.date, "%Y-%m-%d").replace(hour=23, minute=59)

    return result.astimezone(target_timezone).isoformat()


class Task(BaseTask):
    @property
    def labels_str(self):
        result = " ".join(self.labels) if self.labels else ""
        if not self.due:
            result += " non-urgent"
        return result

    def __gt__(self, other):
        if not self.due and not other.due:
            return self.id > other.id
        elif not self.due:
            return True
        elif not other.due:
            return False

        return convert_to_timezone(self.due) > convert_to_timezone(other.due)
