"""Reference answers for 01_data_structures.py.

Kept out of the topic file so solving a question doesn't spoil it.
Shown only by `--answers` mode via ANSWERS[func_name]."""

from collections import defaultdict
import os, sys


ANSWERS = {
    "mix_indexed": lambda l1, l2: l1[1::2] + l2[0::2],
    "reverse_chunks": lambda lst: [lst[i:i + len(lst) // 3][::-1]
                        for i in range(0, len(lst), len(lst) // 3)],
    "count_elements": lambda lst: {x: lst.count(x) for x in lst},
    "paired_set": lambda a, b: set(zip(a, b)),
    "common_elements": lambda a, b: a & b,
    "is_subset": lambda a, b: a.issubset(b),
    "filter_by_values": lambda lst, d: [x for x in lst if x in d.values()],
    "unique_values": lambda d: list(dict.fromkeys(d.values())),
    "unique_tuple": lambda lst: tuple(dict.fromkeys(lst)),
    "min_max": lambda lst: (min(lst), max(lst)),
}
