from os import getenv


class Config:
    TODOIST_API_KEY = getenv("TODOIST_API_KEY")

    if not TODOIST_API_KEY:
        raise EnvironmentError("The environment variable `TODOIST_API_KEY` is not set.")
