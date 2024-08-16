from datetime import timedelta, date


TODAY = date.today()


TOMORROW = TODAY + timedelta(days=1)


LIST_HELP = """\b
Lists all open tasks grouped and ordered by due date

aliases=list,ls
"""
