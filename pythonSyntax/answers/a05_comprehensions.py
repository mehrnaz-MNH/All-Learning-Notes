"""Reference answers for 05_comprehensions.py.

Kept out of the topic file so solving a question doesn't spoil it.
Shown only by `--answers` mode via ANSWERS[func_name]."""

import os, sys


ANSWERS = {
    "squares": lambda n: [x * x for x in range(1, n + 1)],
    "only_evens": lambda nums: [n for n in nums if n % 2 == 0],
    "flatten": lambda matrix: [x for row in matrix for x in row],
    "squares_of_odds": lambda nums: [n * n for n in nums if n % 2 == 1],
    "word_frequency": lambda words: {w: words.count(w) for w in set(words)},
    "passing_scores": lambda scores: {k: v for k, v in scores.items() if v >= 50},
    "unique_vowels": lambda s: {c for c in s if c in "aeiou"},
    "common_elements": lambda a, b: {x for x in a if x in set(b)},
    "transpose": lambda m: [[row[i] for row in m] for i in range(len(m[0]))],
    "cartesian_product": lambda xs, ys: [(x, y) for x in xs for y in ys],
}
