"""Reference answers for 14_itertools_functools.py.

Kept out of the topic file so solving a question doesn't spoil it.
Shown only by `--answers` mode via ANSWERS[func_name]."""

import os, sys
import itertools, functools


@functools.lru_cache(maxsize=None)
def _fib(n):
    return n if n < 2 else _fib(n - 1) + _fib(n - 2)


ANSWERS = {
    "all_permutations": lambda seq, r: list(itertools.permutations(seq, r)),
    "all_combinations": lambda seq, r: list(itertools.combinations(seq, r)),
    "cartesian_product": lambda a, b: list(itertools.product(a, b)),
    "chain_lists": lambda lists: list(itertools.chain.from_iterable(lists)),
    "counter_slice": lambda start, step, n: list(itertools.islice(itertools.count(start, step), n)),
    "group_consecutive": lambda seq: [(k, list(g)) for k, g in itertools.groupby(seq)],
    "product_reduce": lambda nums: functools.reduce(lambda x, y: x * y, nums, 1),
    "powers_of_two": lambda exps: list(map(functools.partial(pow, 2), exps)),
    "fib_cached": lambda n: _fib(n),
    "sort_versions": lambda versions: sorted(
        versions,
        key=functools.cmp_to_key(
            lambda a, b: (
                (tuple(map(int, a.split('.'))) > tuple(map(int, b.split('.'))))
                - (tuple(map(int, a.split('.'))) < tuple(map(int, b.split('.'))))
            )
        ),
    ),
}
