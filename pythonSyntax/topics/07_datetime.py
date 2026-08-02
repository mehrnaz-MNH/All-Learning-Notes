"""
Topic: Date and Time
Source: https://pynative.com/python-date-and-time-exercise/

Fill in each function body (replace `unimplemented()`), then run:
    python topics/07_datetime.py            # grade your solutions
    python topics/07_datetime.py --answers  # show the answer key

NOTE: Every exercise takes EXPLICIT date inputs (date strings or y/m/d
numbers) so the results are deterministic. Do NOT use datetime.now() or
date.today() anywhere in your solutions.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from harness import Quiz, unimplemented
from answers.a07_datetime import ANSWERS
from datetime import datetime, date, timedelta

quiz = Quiz("Date and Time")


# Q1 -------------------------------------------------------------------------
# Given a year, month and day (as integers), return the full weekday NAME of
# that date as a string, e.g. "Monday", "Tuesday", ... (use strftime("%A")).
#   (2025, 1, 15) -> "Wednesday"
@quiz.question(
    "Return the weekday name (e.g. 'Wednesday') for a given (year, month, day).",
    cases=[
        ((2025, 1, 15), "Wednesday"),
        ((2024, 2, 29), "Thursday"),  # leap-day edge case
    ],
    answer=ANSWERS["weekday_name"],
)
def weekday_name(y, m, d):
    return unimplemented()


# Q2 -------------------------------------------------------------------------
# Parse a human-written date string of the form "20 January, 2025"
# (format "%d %B, %Y") and re-format it as an ISO string "%Y-%m-%d".
#   "20 January, 2025" -> "2025-01-20"
@quiz.question(
    "Parse a 'DD Month, YYYY' string and re-format it as 'YYYY-MM-DD'.",
    cases=[
        (("20 January, 2025",), "2025-01-20"),
        (("05 March, 2020",), "2020-03-05"),
    ],
    answer=ANSWERS["parse_and_reformat"],
)
def parse_and_reformat(s):
    return unimplemented()


# Q3 -------------------------------------------------------------------------
# Given an ISO date string "YYYY-MM-DD" and an integer n, add n days to the
# date (using timedelta) and return the resulting date as "YYYY-MM-DD".
#   ("2025-03-15", 7) -> "2025-03-22"
@quiz.question(
    "Add n days to an ISO date string and return the new 'YYYY-MM-DD' string.",
    cases=[
        (("2025-03-15", 7), "2025-03-22"),
        (("2025-12-31", 1), "2026-01-01"),  # rolls over into the next year
    ],
    answer=ANSWERS["add_days"],
)
def add_days(s, n):
    return unimplemented()


# Q4 -------------------------------------------------------------------------
# Given two ISO date strings (start, end), return the number of days between
# them as an integer (end minus start).
#   ("2025-01-01", "2025-01-31") -> 30
@quiz.question(
    "Return the integer number of days between two ISO dates (end - start).",
    cases=[
        (("2025-01-01", "2025-01-31"), 30),
        (("2024-02-28", "2024-03-01"), 2),  # spans the leap day 2024-02-29
    ],
    answer=ANSWERS["days_between"],
)
def days_between(a, b):
    return unimplemented()


# Q5 -------------------------------------------------------------------------
# Given a year, month and day, return the day-of-year (ordinal day) as an int:
# how many days into the year that date is (Jan 1 is day 1).
#   (2025, 3, 15) -> 74
@quiz.question(
    "Return the day-of-year (1..366) for a given (year, month, day).",
    cases=[
        ((2025, 3, 15), 74),
        ((2024, 3, 15), 75),  # leap year -> one extra day counted in Feb
    ],
    answer=ANSWERS["day_of_year"],
)
def day_of_year(y, m, d):
    return unimplemented()


# Q6 -------------------------------------------------------------------------
# Given a year, month and day, return the FIRST day of that month as an ISO
# string "YYYY-MM-01".
#   (2025, 8, 17) -> "2025-08-01"
@quiz.question(
    "Return the first day of the month for a given date as 'YYYY-MM-01'.",
    cases=[
        ((2025, 8, 17), "2025-08-01"),
        ((2020, 12, 31), "2020-12-01"),
    ],
    answer=ANSWERS["first_day_of_month"],
)
def first_day_of_month(y, m, d):
    return unimplemented()


# Q7 -------------------------------------------------------------------------
# Given a year and month, return the LAST day of that month as an ISO string.
# Trick: go to the first day of the NEXT month, then subtract one day.
#   (2024, 2) -> "2024-02-29"   (2025, 12) -> "2025-12-31"
@quiz.question(
    "Return the last calendar day of a given (year, month) as 'YYYY-MM-DD'.",
    cases=[
        ((2024, 2), "2024-02-29"),   # leap February
        ((2025, 12), "2025-12-31"),  # December -> next month is next year
    ],
    answer=ANSWERS["last_day_of_month"],
)
def last_day_of_month(y, m):
    return unimplemented()


# Q8 -------------------------------------------------------------------------
# Given an ISO date string and a target weekday (0=Monday ... 6=Sunday),
# return the NEXT date (strictly after the given one) that falls on that
# weekday, as "YYYY-MM-DD". If the given date is already that weekday, jump a
# full week ahead.
#   ("2025-07-23", 4) -> "2025-07-25"   (Wed -> next Friday)
@quiz.question(
    "Return the next date (strictly after) landing on target weekday (0=Mon..6=Sun).",
    cases=[
        (("2025-07-23", 4), "2025-07-25"),  # Wednesday -> upcoming Friday
        (("2025-07-21", 0), "2025-07-28"),  # already Monday -> Monday next week
    ],
    answer=ANSWERS["next_weekday"],
)
def next_weekday(s, t):
    return unimplemented()


# Q9 -------------------------------------------------------------------------
# Given two ISO date strings (start, end) INCLUSIVE, count how many are
# weekdays (Monday-Friday), i.e. business days, and return that int.
#   ("2025-07-01", "2025-07-31") -> 23
@quiz.question(
    "Count business days (Mon-Fri) between two ISO dates, inclusive.",
    cases=[
        (("2025-07-01", "2025-07-31"), 23),
        (("2025-07-05", "2025-07-06"), 0),  # Sat + Sun only -> zero
    ],
    answer=ANSWERS["business_days"],
)
def business_days(a, b):
    return unimplemented()


# Q10 ------------------------------------------------------------------------
# Given two datetime strings "YYYY-MM-DD HH:MM:SS" (start, end), return the
# difference in total seconds as a float (end - start), via total_seconds().
#   ("2025-01-01 00:00:00", "2025-01-01 02:45:30") -> 9930.0
@quiz.question(
    "Return the difference between two 'YYYY-MM-DD HH:MM:SS' datetimes in seconds (float).",
    cases=[
        (("2025-01-01 00:00:00", "2025-01-01 02:45:30"), 9930.0),
        (("2025-01-01 00:00:00", "2025-01-01 00:00:00"), 0.0),
    ],
    answer=ANSWERS["seconds_between"],
)
def seconds_between(a, b):
    return unimplemented()


if __name__ == "__main__":
    quiz.run()
