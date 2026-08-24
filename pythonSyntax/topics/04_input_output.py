"""
Topic: Input and Output
Source: https://pynative.com/python-input-and-output-exercise/

Real input()/print() can't be graded, so every exercise here is reframed as a
pure string-FORMATTING function: it RETURNS the exact string that would have
been printed (number formatting, alignment/padding, f-strings, decimals, and
parsing input strings). Nothing actually reads input or prints.

Fill in each function body (replace `unimplemented()`), then run:
    python topics/04_input_output.py            # grade your solutions
    python topics/04_input_output.py --answers  # show the answer key
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from harness import Quiz, unimplemented
from answers.a04_input_output import ANSWERS

quiz = Quiz("Input and Output")


# Q1 -------------------------------------------------------------------------
# Given two integers, RETURN the sentence describing their product.
# Example: a=20, b=10 -> "The multiplication is: 200"
# (a single-line string, no trailing newline)
@quiz.question(
    "Return 'The multiplication is: N' where N is a*b.",
    cases=[
        ((20, 10), "The multiplication is: 200"),
        ((0, 5), "The multiplication is: 0"),
    ],
    answer=ANSWERS["multiplication_message"],
)
def multiplication_message(a, b):
    return 'The multiplication is:' + (a*b)


# Q2 -------------------------------------------------------------------------
# Join three words with three asterisks '***' between them (no spaces).
# Example: 'Name','Is','James' -> "Name***Is***James"
@quiz.question(
    "Return the three words joined by '***'.",
    cases=[
        (("Name", "Is", "James"), "Name***Is***James"),
        (("A", "B", "C"), "A***B***C"),
    ],
    answer=ANSWERS["star_join"],
)
def star_join(a, b, c):
    return a+'***'+b+'***'+c


# Q3 -------------------------------------------------------------------------
# Return the binary-representation sentence for a non-negative integer n.
# Example: n=45 -> "The binary representation of 45 is 101101"
# (no '0b' prefix; use format spec 'b')
@quiz.question(
    "Return 'The binary representation of N is <bits>' with no 0b prefix.",
    cases=[
        ((45,), "The binary representation of 45 is 101101"),
        ((0,), "The binary representation of 0 is 0"),
    ],
    answer=ANSWERS["to_binary"],
)
def to_binary(n):
    return "The binary representation of " + n + " is " + format(n , 'b')


# Q4 -------------------------------------------------------------------------
# Return the hexadecimal sentence for a non-negative integer n.
# Lowercase hex digits, no '0x' prefix.
# Example: n=255 -> "The hexadecimal value is ff"
@quiz.question(
    "Return 'The hexadecimal value is <hex>' (lowercase, no 0x prefix).",
    cases=[
        ((255,), "The hexadecimal value is ff"),
        ((16,), "The hexadecimal value is 10"),
    ],
    answer=ANSWERS["to_hex"],
)
def to_hex(n):
    return 'The hexadecimal value is ' + format(n , 'x')


# Q5 -------------------------------------------------------------------------
# Compute numerator/denominator * 100 as a percentage, formatted to exactly
# two decimal places and suffixed with '%'.
# Example: num=2200, den=2900 -> "The result is: 75.86%"
@quiz.question(
    "Return 'The result is: X.XX%' for num/den*100, 2 decimal places.",
    cases=[
        ((2200, 2900), "The result is: 75.86%"),
        ((1, 2), "The result is: 50.00%"),
    ],
    answer=ANSWERS["percentage"],
)
def percentage(num, den):
    res = num/den * 100
    return f"Return 'The result is: {res:.2f}"


# Q6 -------------------------------------------------------------------------
# Right-align a word within a total field width of 20 characters, padding the
# LEFT with spaces. The returned string is exactly 20 chars (when word <= 20).
# Example: 'PyNative' -> "            PyNative"  (12 leading spaces)
@quiz.question(
    "Return the word right-aligned in a field of width 20 (space padded).",
    cases=[
        (("PyNative",), " " * 12 + "PyNative"),
        (("Hi",), " " * 18 + "Hi"),
    ],
    answer=ANSWERS["right_align"],
)
def right_align(word):
    return unimplemented()


# Q7 -------------------------------------------------------------------------
# Center a string within a 40-character field, padding with hyphens '-'.
# Example: 'REPORT SUMMARY' -> "-------------REPORT SUMMARY-------------"
# (13 hyphens on each side; text length 14)
@quiz.question(
    "Return the text centered in a width-40 field, padded with '-'.",
    cases=[
        (("REPORT SUMMARY",), "-" * 13 + "REPORT SUMMARY" + "-" * 13),
        (("HI",), "-" * 19 + "HI" + "-" * 19),
    ],
    answer=ANSWERS["center_dashes"],
)
def center_dashes(text):
    return unimplemented()


# Q8 -------------------------------------------------------------------------
# Return a number as a string padded with LEADING zeros to a total width of 5.
# Example: 42 -> "00042"   ;   12345 -> "12345"
@quiz.question(
    "Return n as a 5-character string, zero-padded on the left.",
    cases=[
        ((42,), "00042"),
        ((0,), "00000"),
    ],
    answer=ANSWERS["zero_pad"],
)
def zero_pad(n):
    return unimplemented()


# Q9 -------------------------------------------------------------------------
# Format a money amount as currency: a '$' sign, commas grouping thousands, and
# exactly two decimal places. Return the full labelled sentence.
# Example: 1250500.7 -> "Total Balance: $1,250,500.70"
@quiz.question(
    "Return 'Total Balance: $X,XXX,XXX.XX' with thousands commas and 2 decimals.",
    cases=[
        ((1250500.7,), "Total Balance: $1,250,500.70"),
        ((0,), "Total Balance: $0.00"),
    ],
    answer=ANSWERS["currency"],
)
def currency(amount):
    return unimplemented()


# Q10 ------------------------------------------------------------------------
# Parse a single space-separated input string of exactly three names and return
# a THREE-LINE string labelling each. Lines are separated by '\n' with NO
# trailing newline.
# Example: "Emma Jessa Kelly" -> "Name1: Emma\nName2: Jessa\nName3: Kelly"
@quiz.question(
    "Split a 3-name string and return 'Name1: a\\nName2: b\\nName3: c'.",
    cases=[
        (("Emma Jessa Kelly",), "Name1: Emma\nName2: Jessa\nName3: Kelly"),
        (("A B C",), "Name1: A\nName2: B\nName3: C"),
    ],
    answer=ANSWERS["label_names"],
)
def label_names(s):
    return unimplemented()


if __name__ == "__main__":
    quiz.run()
