"""Reference answers for 04_input_output.py.

Kept out of the topic file so solving a question doesn't spoil it.
Shown only by `--answers` mode via ANSWERS[func_name]."""

import os, sys


ANSWERS = {
    "multiplication_message": lambda a, b: f"The multiplication is: {a * b}",
    "star_join": lambda a, b, c: "***".join([a, b, c]),
    "to_binary": lambda n: f"The binary representation of {n} is {n:b}",
    "to_hex": lambda n: f"The hexadecimal value is {n:x}",
    "percentage": lambda num, den: f"The result is: {num / den * 100:.2f}%",
    "right_align": lambda word: word.rjust(20),
    "center_dashes": lambda text: text.center(40, "-"),
    "zero_pad": lambda n: f"{n:05d}",
    "currency": lambda amount: f"Total Balance: ${amount:,.2f}",
    "label_names": lambda s: "\n".join(
        f"Name{i}: {name}" for i, name in enumerate(s.split(), 1)
    ),
}
