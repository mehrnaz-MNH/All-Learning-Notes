"""Reference answers for 16_intermediate.py.

Kept out of the topic file so solving a question doesn't spoil it.
Shown only by `--answers` mode via ANSWERS[func_name]."""

import os, sys


def _flatten(lst):
    """Recursively flatten arbitrarily nested lists into a flat list."""
    out = []
    for x in lst:
        if isinstance(x, list):
            out.extend(_flatten(x))
        else:
            out.append(x)
    return out


def _rotate_right(lst, n):
    """Return a new list rotated right by n positions."""
    if not lst:
        return []
    n %= len(lst)
    return lst[-n:] + lst[:-n] if n else lst[:]


def _summarize(*args, **kwargs):
    """Collapse variable positional/keyword args into a summary tuple."""
    return (len(args), sum(args), sorted(kwargs.items()))


def _double(func):
    """Decorator: run `func` and double whatever number it returns."""
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) * 2
    return wrapper


def _rank_by_score(names, scores):
    """Pair names with scores, sort by score descending, number from 1."""
    paired = sorted(zip(names, scores), key=lambda p: -p[1])
    return [(rank, name) for rank, (name, _score) in enumerate(paired, 1)]


ANSWERS = {
    "flatten": _flatten,
    "is_anagram": lambda a, b: sorted(a.lower()) == sorted(b.lower()),
    "reverse_each_word": lambda s: " ".join(w[::-1] for w in s.split(" ")),
    "is_palindrome_sentence": lambda s: (lambda t: t == t[::-1])(
        "".join(c.lower() for c in s if c.isalnum())
    ),
    "dedupe_preserve_order": lambda lst: list(dict.fromkeys(lst)),
    "rotate_right": _rotate_right,
    "even_squares": lambda nums: list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, nums))),
    "summarize_args": lambda args, kwargs: _summarize(*args, **kwargs),
    "decorated_add": lambda a, b: _double(lambda x, y: x + y)(a, b),
    "rank_by_score": _rank_by_score,
}
