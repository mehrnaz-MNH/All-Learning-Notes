"""
Topic: Exception Handling
Source: https://pynative.com/python-exception-handling-exercises/

Fill in each function body (replace `unimplemented()`), then run:
    python topics/12_exception_handling.py            # grade your solutions
    python topics/12_exception_handling.py --answers  # show the answer key

NOTE: every function RETURNS a value describing the outcome. A failed
operation should be caught INSIDE the function and turned into the
sentinel/return value described in each comment -- never let it propagate.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from harness import Quiz, unimplemented
from answers.a12_exception_handling import ANSWERS

quiz = Quiz("Exception Handling")


# A custom exception used by Q8. Defined at module level so both your
# solution and the answer key can raise/catch it.
class NegativeAgeError(Exception):
    """Raised when an age is negative."""
    pass


# Q1 -------------------------------------------------------------------------
# Convert a string to an int with try/except. If the string is a valid
# integer, return the int. If int() raises ValueError (e.g. "abc"), catch it
# and return the string 'error'.
#   "42" -> 42 ;  "abc" -> 'error'
@quiz.question(
    "Convert a string to int; return the int, or 'error' on ValueError.",
    cases=[
        (("42",), 42),
        (("abc",), 'error'),
    ],
    answer=ANSWERS["string_to_int"],
)
def string_to_int(s):
    return unimplemented()


# Q2 -------------------------------------------------------------------------
# Safely divide a by b. Return a / b normally, but if b is 0 catch the
# ZeroDivisionError and return None instead of crashing.
#   (10, 2) -> 5.0 ;  (1, 0) -> None
@quiz.question(
    "Divide a by b; return the quotient, or None on ZeroDivisionError.",
    cases=[
        ((10, 2), 5.0),
        ((1, 0), None),
    ],
    answer=ANSWERS["safe_divide"],
)
def safe_divide(a, b):
    return unimplemented()


# Q3 -------------------------------------------------------------------------
# Return the element of `lst` at position `idx`. If `idx` is out of range,
# catch IndexError and return the string 'out of range'.
#   ([1,2,3], 1) -> 2 ;  ([1,2,3], 9) -> 'out of range'
@quiz.question(
    "Return lst[idx], or 'out of range' on IndexError.",
    cases=[
        (([1, 2, 3], 1), 2),
        (([1, 2, 3], 9), 'out of range'),
    ],
    answer=ANSWERS["get_at"],
)
def get_at(lst, idx):
    return unimplemented()


# Q4 -------------------------------------------------------------------------
# Look up `key` in dict `d`. Return the value, but if the key is absent catch
# KeyError and return the string 'missing'.
#   ({'a':1}, 'a') -> 1 ;  ({'a':1}, 'x') -> 'missing'
@quiz.question(
    "Return d[key], or 'missing' on KeyError.",
    cases=[
        (({'a': 1, 'b': 2}, 'a'), 1),
        (({'a': 1, 'b': 2}, 'x'), 'missing'),
    ],
    answer=ANSWERS["get_value"],
)
def get_value(d, key):
    return unimplemented()


# Q5 -------------------------------------------------------------------------
# Add a and b. Return the sum, but if the two types cannot be added (e.g.
# int + str) catch TypeError and return the string 'TypeError'.
#   (2, 3) -> 5 ;  (2, 'x') -> 'TypeError'
@quiz.question(
    "Return a + b, or 'TypeError' when the types can't be added.",
    cases=[
        ((2, 3), 5),
        ((2, 'x'), 'TypeError'),
    ],
    answer=ANSWERS["safe_add"],
)
def safe_add(a, b):
    return unimplemented()


# Q6 -------------------------------------------------------------------------
# Both a and b are strings. Convert them to ints and return a / b. Use two
# separate except clauses: return 'invalid' if conversion fails (ValueError)
# and 'zero' if dividing by zero (ZeroDivisionError).
#   ('10','2') -> 5.0 ;  ('x','2') -> 'invalid' ;  ('10','0') -> 'zero'
@quiz.question(
    "Parse two strings and divide; 'invalid' on ValueError, 'zero' on ZeroDivisionError.",
    cases=[
        (("10", "2"), 5.0),
        (("x", "2"), 'invalid'),
        (("10", "0"), 'zero'),
    ],
    answer=ANSWERS["parse_and_divide"],
)
def parse_and_divide(a, b):
    return unimplemented()


# Q7 -------------------------------------------------------------------------
# Compute a / b just to see what happens. If it raises, return the NAME of the
# exception type via type(exc).__name__. If it succeeds, return 'ok'.
#   (1, 0) -> 'ZeroDivisionError' ;  (6, 3) -> 'ok'
@quiz.question(
    "Return the raised exception's type name for a / b, or 'ok' if none.",
    cases=[
        ((1, 0), 'ZeroDivisionError'),
        ((6, 3), 'ok'),
    ],
    answer=ANSWERS["raised_name"],
)
def raised_name(a, b):
    return unimplemented()


# Q8 -------------------------------------------------------------------------
# Validate an age using a CUSTOM exception. If age is negative, raise the
# module-level NegativeAgeError, catch it internally, and return the string
# 'NegativeAgeError'. If age is valid (>= 0), return the age unchanged.
#   25 -> 25 ;  -5 -> 'NegativeAgeError'
@quiz.question(
    "Raise+catch a custom NegativeAgeError for negative age; else return the age.",
    cases=[
        ((25,), 25),
        ((-5,), 'NegativeAgeError'),
    ],
    answer=ANSWERS["validate_age"],
)
def validate_age(age):
    return unimplemented()


# Q9 -------------------------------------------------------------------------
# Use try/except/finally. Divide a by b: on success return 'result:<value>'
# (e.g. 'result:5.0'); on ZeroDivisionError return 'error'. The value is built
# in the try/except, so a plain finally-based cleanup does not change it.
#   (10, 2) -> 'result:5.0' ;  (1, 0) -> 'error'
@quiz.question(
    "Divide with try/except/finally; 'result:<value>' on success, 'error' on divide-by-zero.",
    cases=[
        ((10, 2), 'result:5.0'),
        ((1, 0), 'error'),
    ],
    answer=ANSWERS["divide_with_cleanup"],
)
def divide_with_cleanup(a, b):
    return unimplemented()


# Q10 ------------------------------------------------------------------------
# Use try/except/else. Convert string s to int in the try. If it fails, return
# 'invalid'. Otherwise (else clause) return the number if it is positive, or
# 'not positive' if it is zero or negative.
#   '5' -> 5 ;  'abc' -> 'invalid' ;  '-3' -> 'not positive'
@quiz.question(
    "try/except/else: 'invalid' on bad parse, else the number or 'not positive'.",
    cases=[
        (("5",), 5),
        (("abc",), 'invalid'),
        (("-3",), 'not positive'),
    ],
    answer=ANSWERS["parse_positive"],
)
def parse_positive(s):
    return unimplemented()


if __name__ == "__main__":
    quiz.run()
