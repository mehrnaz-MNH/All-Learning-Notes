"""Reference answers for 03_sets.py.

Kept out of the topic file so solving a question doesn't spoil it.
Shown only by `--answers` mode via ANSWERS[func_name]."""

import os, sys


ANSWERS = {
    "set_union": lambda a, b: a | b,
    "set_intersection": lambda a, b: a & b,
    "set_difference": lambda a, b: a - b,
    "set_symmetric_difference": lambda a, b: a ^ b,
    "is_subset": lambda a, b: a.issubset(b),
    "is_disjoint": lambda a, b: a.isdisjoint(b),
    "add_item": lambda s, item: s | {item},
    "common_in_lists": lambda xs, ys: set(xs) & set(ys),
    "dedupe_keep_order": lambda xs: list(dict.fromkeys(xs)),
    "divisible_by_three": lambda s: {n for n in s if n % 3 == 0},
}
