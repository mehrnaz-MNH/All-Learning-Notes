"""Reference answers for 12_exception_handling.py.

Kept out of the topic file so solving a question doesn't spoil it.
Shown only by `--answers` mode via ANSWERS[func_name]."""

import os, sys


class NegativeAgeError(Exception):
    """Raised when an age is negative."""
    pass


def _string_to_int_ans(s):
    try:
        return int(s)
    except ValueError:
        return 'error'


def _safe_divide_ans(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


def _get_at_ans(lst, idx):
    try:
        return lst[idx]
    except IndexError:
        return 'out of range'


def _get_value_ans(d, key):
    try:
        return d[key]
    except KeyError:
        return 'missing'


def _safe_add_ans(a, b):
    try:
        return a + b
    except TypeError:
        return 'TypeError'


def _parse_and_divide_ans(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'invalid'
    except ZeroDivisionError:
        return 'zero'


def _raised_name_ans(a, b):
    try:
        a / b
    except Exception as exc:
        return type(exc).__name__
    return 'ok'


def _validate_age_ans(age):
    try:
        if age < 0:
            raise NegativeAgeError("age must be >= 0")
        return age
    except NegativeAgeError as exc:
        return type(exc).__name__


def _divide_with_cleanup_ans(a, b):
    try:
        result = a / b
        return 'result:' + str(result)
    except ZeroDivisionError:
        return 'error'
    finally:
        _divide_with_cleanup_ans.last = 'cleanup'  # runs in both paths


def _parse_positive_ans(s):
    try:
        n = int(s)
    except ValueError:
        return 'invalid'
    else:
        return n if n > 0 else 'not positive'


ANSWERS = {
    "string_to_int": _string_to_int_ans,
    "safe_divide": _safe_divide_ans,
    "get_at": _get_at_ans,
    "get_value": _get_value_ans,
    "safe_add": _safe_add_ans,
    "parse_and_divide": _parse_and_divide_ans,
    "raised_name": _raised_name_ans,
    "validate_age": _validate_age_ans,
    "divide_with_cleanup": _divide_with_cleanup_ans,
    "parse_positive": _parse_positive_ans,
}
