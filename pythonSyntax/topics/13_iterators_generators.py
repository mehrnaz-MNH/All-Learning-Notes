"""
Topic: Iterators and Generators
Source: https://pynative.com/python-iterators-generators-exercises/

Fill in each function body (replace `unimplemented()`), then run:
    python topics/13_iterators_generators.py            # grade your solutions
    python topics/13_iterators_generators.py --answers  # show the answer key
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from harness import Quiz, unimplemented
from answers.a13_iterators_generators import ANSWERS

quiz = Quiz("Iterators and Generators")


# Q1 -------------------------------------------------------------------------
# Write a generator that yields the squares of 1..n (inclusive), then collect
# the produced values into a list.
#   n=4 -> [1, 4, 9, 16]
# Return value is a materialized list (never the generator object itself).
@quiz.question(
    "Square generator: return the squares of 1..n as a list.",
    cases=[
        ((4,), [1, 4, 9, 16]),
        ((1,), [1]),
        ((0,), []),
    ],
    answer=ANSWERS["squares"],
)
def squares(n):
    return unimplemented()


# Q2 -------------------------------------------------------------------------
# Build a class-based iterator (with __iter__/__next__) that produces the
# first `count` even numbers starting at 0, then return list(it).
#   count=5 -> [0, 2, 4, 6, 8]
# Return value is a materialized list.
@quiz.question(
    "Even-number iterator class: return the first `count` even numbers as a list.",
    cases=[
        ((5,), [0, 2, 4, 6, 8]),
        ((1,), [0]),
        ((0,), []),
    ],
    answer=ANSWERS["even_numbers"],
)
def even_numbers(count):
    return unimplemented()


# Q3 -------------------------------------------------------------------------
# Reimplement range() as a generator supporting a custom step, yielding values
# from start (inclusive) up to stop (exclusive). Return the values as a list.
#   start=1, stop=10, step=2 -> [1, 3, 5, 7, 9]
# Return value is a materialized list.
@quiz.question(
    "Custom range generator with step: return the produced values as a list.",
    cases=[
        ((1, 10, 2), [1, 3, 5, 7, 9]),
        ((0, 5, 1), [0, 1, 2, 3, 4]),
        ((5, 5, 1), []),
    ],
    answer=ANSWERS["custom_range"],
)
def custom_range(start, stop, step):
    return unimplemented()


# Q4 -------------------------------------------------------------------------
# Build a class-based iterator that walks a string in reverse, yielding one
# character at a time, then return list(it).
#   "abc" -> ['c', 'b', 'a']
# Return value is a materialized list of single characters.
@quiz.question(
    "Reverse-string iterator class: return the characters in reverse order as a list.",
    cases=[
        (("abc",), ['c', 'b', 'a']),
        (("hi",), ['i', 'h']),
        (("",), []),
    ],
    answer=ANSWERS["reverse_string"],
)
def reverse_string(s):
    return unimplemented()


# Q5 -------------------------------------------------------------------------
# Write a generator that acts as a filter, yielding only the vowels (aeiou,
# case-insensitive) from the input string. Return them as a list.
#   "Hello World" -> ['e', 'o', 'o']
# Return value is a materialized list.
@quiz.question(
    "Vowel filter generator: return only the vowels from the string as a list.",
    cases=[
        (("Hello World",), ['e', 'o', 'o']),
        (("AEIOU",), ['A', 'E', 'I', 'O', 'U']),
        (("xyz",), []),
    ],
    answer=ANSWERS["vowels"],
)
def vowels(s):
    return unimplemented()


# Q6 -------------------------------------------------------------------------
# Use a generator EXPRESSION (parentheses syntax) to produce the powers of two
# 2**0 .. 2**(n-1), then collect them into a list.
#   n=5 -> [1, 2, 4, 8, 16]
# Return value is a materialized list.
@quiz.question(
    "Powers of two via a generator expression: return the first n powers as a list.",
    cases=[
        ((5,), [1, 2, 4, 8, 16]),
        ((1,), [1]),
        ((0,), []),
    ],
    answer=ANSWERS["powers_of_two"],
)
def powers_of_two(n):
    return unimplemented()


# Q7 -------------------------------------------------------------------------
# Write a stateful Fibonacci generator that yields the first n Fibonacci
# numbers (starting 0, 1, 1, 2, ...), then return them as a list.
#   n=5 -> [0, 1, 1, 2, 3]
# Return value is a materialized list.
@quiz.question(
    "Fibonacci generator: return the first n Fibonacci numbers as a list.",
    cases=[
        ((5,), [0, 1, 1, 2, 3]),
        ((1,), [0]),
        ((0,), []),
    ],
    answer=ANSWERS["fibonacci"],
)
def fibonacci(n):
    return unimplemented()


# Q8 -------------------------------------------------------------------------
# Create an INFINITE counter generator (while True) that counts up from
# `start`, then use itertools.islice to take only the first n values and
# return them as a list.
#   start=10, n=4 -> [10, 11, 12, 13]
# Return value is a materialized list (the generator itself never terminates).
@quiz.question(
    "Infinite counter sliced with itertools.islice: return the first n values as a list.",
    cases=[
        ((10, 4), [10, 11, 12, 13]),
        ((0, 3), [0, 1, 2]),
        ((5, 0), []),
    ],
    answer=ANSWERS["take_count"],
)
def take_count(start, n):
    return unimplemented()


# Q9 -------------------------------------------------------------------------
# Write a recursive generator that flattens an arbitrarily nested list using
# `yield from`, then return the flattened values as a list.
#   [1, [2, [3, 4], 5]] -> [1, 2, 3, 4, 5]
# Return value is a materialized flat list.
@quiz.question(
    "Flatten a nested list with `yield from`: return a flat list.",
    cases=[
        (([1, [2, [3, 4], 5]],), [1, 2, 3, 4, 5]),
        (([[1], [2, 3], [[4]]],), [1, 2, 3, 4]),
        (([],), []),
    ],
    answer=ANSWERS["flatten"],
)
def flatten(nested):
    return unimplemented()


# Q10 ------------------------------------------------------------------------
# Write a generator that groups items from an iterable into fixed-size batches
# (the final batch may be shorter), then return the batches as a list of lists.
#   items=[1,2,3,4,5], size=2 -> [[1, 2], [3, 4], [5]]
# Return value is a materialized list of lists.
@quiz.question(
    "Batch a stream into fixed-size chunks: return a list of lists.",
    cases=[
        (([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]]),
        (([1, 2, 3, 4], 2), [[1, 2], [3, 4]]),
        (([], 3), []),
    ],
    answer=ANSWERS["batched"],
)
def batched(items, size):
    return unimplemented()


if __name__ == "__main__":
    quiz.run()
