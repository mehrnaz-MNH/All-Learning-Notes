"""Reference answers for 02_dictionaries.py.

Kept out of the topic file so solving a question doesn't spoil it.
Shown only by `--answers` mode via ANSWERS[func_name]."""

import os, sys


ANSWERS = {
    "zip_to_dict": lambda keys, values: dict(zip(keys, values)),
    "merge_dicts": lambda d1, d2: {**d1, **d2},
    "nested_get": lambda d, path: __import__('functools').reduce(lambda acc, k: acc[k], path, d),
    "squares_dict": lambda num: {n: n * n for n in range(1, num + 1)},
    "pick_keys": lambda d, keys: {k: d[k] for k in keys},
    "key_of_min_value": lambda d: min(d, key=d.get),
    "drop_key": lambda d, key: {k: v for k, v in d.items() if k != key},
    "char_frequency": lambda s: {c: s.count(c) for c in s},
    "invert_dict": lambda d: {v: k for k, v in d.items()},
    "sum_values": lambda d: sum(d.values()),
}
