"""
Topic: itertools and functools
Source: https://pynative.com/python-itertools-functools-exercises/

Fill in each function body (replace `unimplemented()`), then run:
    python topics/14_itertools_functools.py            # grade your solutions
    python topics/14_itertools_functools.py --answers  # show the answer key

Note: every answer RETURNS a materialized value -- a list built from the
itertools result (never a bare iterator), or a plain number for the
functools.reduce / lru_cache exercises.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from harness import Quiz, unimplemented
from answers.a14_itertools_functools import ANSWERS

import itertools, functools

quiz = Quiz("itertools and functools")


# Q1 -------------------------------------------------------------------------
# Return ALL r-length permutations (ordered arrangements) of a sequence,
# using itertools.permutations, as a materialized list of tuples.
#   seq=[1,2,3], r=2 -> [(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)]
@quiz.question(
    "Return all r-length permutations of a sequence as a list of tuples.",
    cases=[
        (([1, 2, 3], 2),
         [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]),
        ((['A', 'B'], 2), [('A', 'B'), ('B', 'A')]),
    ],
    answer=ANSWERS["all_permutations"],
)
def all_permutations(seq, r):
    return unimplemented()


# Q2 -------------------------------------------------------------------------
# Return ALL r-length combinations (unordered, no repeats) of a sequence,
# using itertools.combinations, as a materialized list of tuples.
#   seq=[1,2,3,4], r=2 -> [(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
@quiz.question(
    "Return all r-length combinations of a sequence as a list of tuples.",
    cases=[
        (([1, 2, 3, 4], 2),
         [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]),
        (([1, 2, 3], 3), [(1, 2, 3)]),
    ],
    answer=ANSWERS["all_combinations"],
)
def all_combinations(seq, r):
    return unimplemented()


# Q3 -------------------------------------------------------------------------
# Return the Cartesian product of two sequences using itertools.product,
# as a materialized list of (a, b) tuples.
#   a=[1,2], b=['x','y'] -> [(1,'x'),(1,'y'),(2,'x'),(2,'y')]
@quiz.question(
    "Return the Cartesian product of two sequences as a list of tuples.",
    cases=[
        (([1, 2], ['x', 'y']),
         [(1, 'x'), (1, 'y'), (2, 'x'), (2, 'y')]),
        (([1], []), []),
    ],
    answer=ANSWERS["cartesian_product"],
)
def cartesian_product(a, b):
    return unimplemented()


# Q4 -------------------------------------------------------------------------
# Flatten a list of lists into a single sequence using itertools.chain,
# preserving order, and return it as a materialized list.
#   [[1,2],[3],[4,5]] -> [1,2,3,4,5]
@quiz.question(
    "Chain several lists into one flat list, preserving order.",
    cases=[
        (([[1, 2], [3], [4, 5]],), [1, 2, 3, 4, 5]),
        (([[], []],), []),
    ],
    answer=ANSWERS["chain_lists"],
)
def chain_lists(lists):
    return unimplemented()


# Q5 -------------------------------------------------------------------------
# Take the first n values of an infinite arithmetic counter (itertools.count
# with a start and step), sliced with itertools.islice, as a list of ints.
#   start=100, step=5, n=8 -> [100,105,110,115,120,125,130,135]
@quiz.question(
    "Return the first n values of count(start, step) as a list.",
    cases=[
        ((100, 5, 8), [100, 105, 110, 115, 120, 125, 130, 135]),
        ((0, 1, 0), []),
    ],
    answer=ANSWERS["counter_slice"],
)
def counter_slice(start, step, n):
    return unimplemented()


# Q6 -------------------------------------------------------------------------
# Group CONSECUTIVE equal items with itertools.groupby and return a list of
# (value, [items...]) tuples. groupby only groups runs that are adjacent.
#   [1,1,2,3,3,3] -> [(1,[1,1]),(2,[2]),(3,[3,3,3])]
@quiz.question(
    "Group consecutive equal items into a list of (value, group_list) tuples.",
    cases=[
        (([1, 1, 2, 3, 3, 3],), [(1, [1, 1]), (2, [2]), (3, [3, 3, 3])]),
        (([1, 1, 2, 1],), [(1, [1, 1]), (2, [2]), (1, [1])]),
    ],
    answer=ANSWERS["group_consecutive"],
)
def group_consecutive(seq):
    return unimplemented()


# Q7 -------------------------------------------------------------------------
# Reduce a list of numbers to their product using functools.reduce.
# Provide an initial value of 1 so an empty list returns 1.
#   [2,3,4,5,6] -> 720
@quiz.question(
    "Return the product of all numbers in a list using functools.reduce.",
    cases=[
        (([2, 3, 4, 5, 6],), 720),
        (([],), 1),
    ],
    answer=ANSWERS["product_reduce"],
)
def product_reduce(nums):
    return unimplemented()


# Q8 -------------------------------------------------------------------------
# Use functools.partial to fix the base of pow() to 2, then map that partial
# over a list of exponents. Return the powers of two as a materialized list.
#   exponents=[0,1,2,3,4] -> [1,2,4,8,16]   (partial(pow, 2))
@quiz.question(
    "Use functools.partial(pow, 2) to return 2**e for each exponent as a list.",
    cases=[
        (([0, 1, 2, 3, 4],), [1, 2, 4, 8, 16]),
        (([10],), [1024]),
    ],
    answer=ANSWERS["powers_of_two"],
)
def powers_of_two(exps):
    return unimplemented()


# Q9 -------------------------------------------------------------------------
# Compute the nth Fibonacci number using recursion memoised with
# functools.lru_cache (fib(0)=0, fib(1)=1). Return the number.
#   n=10 -> 55 ;  n=0 -> 0
@quiz.question(
    "Return the nth Fibonacci number (memoised recursion with lru_cache).",
    cases=[
        ((10,), 55),
        ((0,), 0),
    ],
    answer=ANSWERS["fib_cached"],
)
def fib_cached(n):
    return unimplemented()


# Q10 ------------------------------------------------------------------------
# Sort version strings NUMERICALLY (not lexicographically) using
# functools.cmp_to_key with a comparator over their integer parts.
# Return the sorted list of strings.
#   ["1.10.2","1.9.1","1.2.3"] -> ["1.2.3","1.9.1","1.10.2"]
#   (lexicographic sort would wrongly put "1.10.2" before "1.9.1")
@quiz.question(
    "Sort dotted version strings numerically using cmp_to_key; return the list.",
    cases=[
        ((["1.10.2", "1.9.1", "2.0.0", "1.2.3", "1.10.10"],),
         ["1.2.3", "1.9.1", "1.10.2", "1.10.10", "2.0.0"]),
        ((["3.0", "1.0", "2.0"],), ["1.0", "2.0", "3.0"]),
    ],
    answer=ANSWERS["sort_versions"],
)
def sort_versions(versions):
    return unimplemented()


if __name__ == "__main__":
    quiz.run()
