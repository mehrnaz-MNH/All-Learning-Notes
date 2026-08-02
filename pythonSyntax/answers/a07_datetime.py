"""Reference answers for 07_datetime.py.

Kept out of the topic file so solving a question doesn't spoil it.
Shown only by `--answers` mode via ANSWERS[func_name]."""

import os, sys
from datetime import datetime, date, timedelta


ANSWERS = {
    "weekday_name": lambda y, m, d: date(y, m, d).strftime("%A"),
    "parse_and_reformat": lambda s: datetime.strptime(s, "%d %B, %Y").strftime("%Y-%m-%d"),
    "add_days": lambda s, n: (datetime.strptime(s, "%Y-%m-%d") + timedelta(days=n)).strftime("%Y-%m-%d"),
    "days_between": lambda a, b: (datetime.strptime(b, "%Y-%m-%d") - datetime.strptime(a, "%Y-%m-%d")).days,
    "day_of_year": lambda y, m, d: date(y, m, d).timetuple().tm_yday,
    "first_day_of_month": lambda y, m, d: date(y, m, d).replace(day=1).strftime("%Y-%m-%d"),
    "last_day_of_month": lambda y, m: ((date(y + 1, 1, 1) if m == 12 else date(y, m + 1, 1)) - timedelta(days=1)).strftime("%Y-%m-%d"),
    "next_weekday": lambda s, t: (
        lambda d: (d + timedelta(days=((t - d.weekday()) % 7) or 7)).strftime("%Y-%m-%d")
    )(datetime.strptime(s, "%Y-%m-%d")),
    "business_days": lambda a, b: (
        lambda da, n: sum(1 for i in range(n) if (da + timedelta(days=i)).weekday() < 5)
    )(datetime.strptime(a, "%Y-%m-%d"),
      (datetime.strptime(b, "%Y-%m-%d") - datetime.strptime(a, "%Y-%m-%d")).days + 1),
    "seconds_between": lambda a, b: (
        datetime.strptime(b, "%Y-%m-%d %H:%M:%S") - datetime.strptime(a, "%Y-%m-%d %H:%M:%S")
    ).total_seconds(),
}
