"""Reference answers for 13_iterators_generators.py.

Kept out of the topic file so solving a question doesn't spoil it.
Shown only by `--answers` mode via ANSWERS[func_name]."""

import os, sys


def _squares_gen(n):
    for i in range(1, n + 1):
        yield i * i


def _custom_range_gen(start, stop, step):
    cur = start
    while cur < stop:
        yield cur
        cur += step


def _vowel_gen(s):
    for ch in s:
        if ch.lower() in "aeiou":
            yield ch


def _fib_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def _count_from(start):
    n = start
    while True:
        yield n
        n += 1


def _flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from _flatten(item)
        else:
            yield item


def _batched(iterable, size):
    batch = []
    for item in iterable:
        batch.append(item)
        if len(batch) == size:
            yield batch
            batch = []
    if batch:
        yield batch


class _EvenIterator:
    """Iterator yielding the first `count` even numbers starting from 0."""
    def __init__(self, count):
        self.count = count
        self.current = 0
        self.produced = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.produced >= self.count:
            raise StopIteration
        value = self.current
        self.current += 2
        self.produced += 1
        return value


class _ReverseStringIterator:
    """Iterator walking a string backwards, one character at a time."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index <= 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


ANSWERS = {
    "squares": lambda n: list(_squares_gen(n)),
    "even_numbers": lambda count: list(_EvenIterator(count)),
    "custom_range": lambda start, stop, step: list(_custom_range_gen(start, stop, step)),
    "reverse_string": lambda s: list(_ReverseStringIterator(s)),
    "vowels": lambda s: list(_vowel_gen(s)),
    "powers_of_two": lambda n: list(2 ** i for i in range(n)),
    "fibonacci": lambda n: list(_fib_gen(n)),
    "take_count": lambda start, n: list(__import__('itertools').islice(_count_from(start), n)),
    "flatten": lambda nested: list(_flatten(nested)),
    "batched": lambda items, size: list(_batched(items, size)),
}
