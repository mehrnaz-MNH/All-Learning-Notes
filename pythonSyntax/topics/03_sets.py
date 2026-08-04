"""
Topic: Sets
Source: https://pynative.com/python-set-exercise-with-solutions/

Fill in each function body (replace `unimplemented()`), then run:
    python topics/03_sets.py            # grade your solutions
    python topics/03_sets.py --answers  # show the answer key
"""
from collections import defaultdict
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from harness import Quiz, unimplemented
from answers.a03_sets import ANSWERS

quiz = Quiz("Sets")


# Q1 -------------------------------------------------------------------------
# Return the UNION of two sets: every element that is in either set.
# Sets are unordered, so returning a set is fine.
#   {1,2,3,4}, {3,4,5,6} -> {1,2,3,4,5,6}
@quiz.question(
    "Return the union of two sets (elements in either set).",
    cases=[
        (({1, 2, 3, 4}, {3, 4, 5, 6}), {1, 2, 3, 4, 5, 6}),
        (({1, 2}, set()), {1, 2}),
    ],
    answer=ANSWERS["set_union"],
)
def set_union(a, b):
    return a | b


# Q2 -------------------------------------------------------------------------
# Return the INTERSECTION of two sets: only elements present in BOTH.
#   {1,2,3,4}, {3,4,5,6} -> {3,4}
@quiz.question(
    "Return the intersection of two sets (elements in both).",
    cases=[
        (({1, 2, 3, 4}, {3, 4, 5, 6}), {3, 4}),
        (({1, 2}, {3, 4}), set()),
    ],
    answer=ANSWERS["set_intersection"],
)
def set_intersection(a, b):
    return a & b


# Q3 -------------------------------------------------------------------------
# Return the DIFFERENCE a - b: elements in `a` that are NOT in `b`.
#   {1,2,3,4}, {3,4,5,6} -> {1,2}
@quiz.question(
    "Return the difference a - b (elements in a but not in b).",
    cases=[
        (({1, 2, 3, 4}, {3, 4, 5, 6}), {1, 2}),
        (({1, 2}, {1, 2, 3}), set()),
    ],
    answer=ANSWERS["set_difference"],
)
def set_difference(a, b):
    return a - b


# Q4 -------------------------------------------------------------------------
# Return the SYMMETRIC DIFFERENCE: elements in either set but NOT in both.
#   {1,2,3,4}, {3,4,5,6} -> {1,2,5,6}
@quiz.question(
    "Return the symmetric difference (elements in exactly one of the two sets).",
    cases=[
        (({1, 2, 3, 4}, {3, 4, 5, 6}), {1, 2, 5, 6}),
        (({1, 2}, {1, 2}), set()),
    ],
    answer=ANSWERS["set_symmetric_difference"],
)
def set_symmetric_difference(a, b):
    return a ^ b


# Q5 -------------------------------------------------------------------------
# Return True if `a` is a SUBSET of `b` (every element of a is also in b).
#   {1,2,3}, {1,2,3,4,5} -> True ;  {1,9}, {1,2,3} -> False
@quiz.question(
    "Return True if set a is a subset of set b.",
    cases=[
        (({1, 2, 3}, {1, 2, 3, 4, 5}), True),
        (({1, 9}, {1, 2, 3}), False),
        ((set(), {1}), True),
    ],
    answer=ANSWERS["is_subset"],
)
def is_subset(a, b):
    return a < b


# Q6 -------------------------------------------------------------------------
# Return True if two sets are DISJOINT (share no common elements).
#   {1,2,3}, {4,5,6} -> True ;  {1,2,3}, {3,4} -> False
@quiz.question(
    "Return True if the two sets have no elements in common (disjoint).",
    cases=[
        (({1, 2, 3}, {4, 5, 6}), True),
        (({1, 2, 3}, {3, 4}), False),
    ],
    answer=ANSWERS["is_disjoint"],
)
def is_disjoint(a, b):
    return  (a & b) == set()


# Q7 -------------------------------------------------------------------------
# Return a NEW set with `item` added, without mutating the input set.
#   {"apple","banana"}, "mango" -> {"apple","banana","mango"}
@quiz.question(
    "Return a new set with `item` added (do not mutate the input).",
    cases=[
        (({"apple", "banana"}, "mango"), {"apple", "banana", "mango"}),
        (({1, 2}, 2), {1, 2}),
    ],
    answer=ANSWERS["add_item"],
)
def add_item(s, item):
    new_set = s
    new_set.add(item)
    return new_set



# Q8 -------------------------------------------------------------------------
# Given two LISTS (which may contain duplicates), return the set of elements
# common to both.  [1,2,3,4,5,3,2], [3,4,5,6,7,4,5] -> {3,4,5}
@quiz.question(
    "Return the set of elements common to both lists.",
    cases=[
        (([1, 2, 3, 4, 5, 3, 2], [3, 4, 5, 6, 7, 4, 5]), {3, 4, 5}),
        (([1, 2], [3, 4]), set()),
    ],
    answer=ANSWERS["common_in_lists"],
)
def common_in_lists(xs, ys):

    return set(xs) & set(ys)


# Q9 -------------------------------------------------------------------------
# Remove duplicates from a list while PRESERVING first-seen order.  Because
# order matters here, return a LIST (not a set).
#   [3,1,4,1,5,9,2,6,5,3,5] -> [3,1,4,5,9,2,6]
@quiz.question(
    "Remove duplicates from a list, preserving first-seen order (return a list).",
    cases=[
        (([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],), [3, 1, 4, 5, 9, 2, 6]),
        (([],), []),
    ],
    answer=ANSWERS["dedupe_keep_order"],
)
def dedupe_keep_order(xs):
     return list(dict.fromkeys(xs))




# Q10 ------------------------------------------------------------------------
# Using a set comprehension, return the set of numbers in the input set that
# are divisible by 3.  {1,2,3,6,7,9,12,14,15} -> {3,6,9,12,15}
@quiz.question(
    "Return the subset of numbers that are divisible by 3.",
    cases=[
        (({1, 2, 3, 6, 7, 9, 12, 14, 15},), {3, 6, 9, 12, 15}),
        (({1, 2, 4},), set()),
    ],
    answer=ANSWERS["divisible_by_three"],
)
def divisible_by_three(s):
    return { num for num in s if num % 3 == 0 }


if __name__ == "__main__":
    quiz.run()
