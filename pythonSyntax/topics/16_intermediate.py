"""
Topic: Intermediate Python (general problem-solving)
Source: https://pynative.com/intermediate-python-exercises/

A catch-all page: functions & recursion, lambda/map/filter, string and list
algorithms, *args/**kwargs, closures/decorators, and zip/enumerate.

Fill in each function body (replace `unimplemented()`), then run:
    python topics/16_intermediate.py            # grade your solutions
    python topics/16_intermediate.py --answers  # show the answer key
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from harness import Quiz, unimplemented
from answers.a16_intermediate import ANSWERS

quiz = Quiz("Intermediate Python")


# Q1 -------------------------------------------------------------------------
# Recursively flatten a list that may contain other lists nested to any depth,
# returning a single flat list in original left-to-right order.
#   [1, [2, 3], [4, [5, 6]], 7] -> [1, 2, 3, 4, 5, 6, 7]
@quiz.question(
    "Recursively flatten an arbitrarily nested list into a flat list.",
    cases=[
        (([1, [2, 3], [4, [5, 6]], 7],), [1, 2, 3, 4, 5, 6, 7]),
        (([[[]]],), []),
    ],
    answer=ANSWERS["flatten"],
)
def flatten(lst):
    return unimplemented()


# Q2 -------------------------------------------------------------------------
# Decide whether two strings are anagrams (same letters, any order),
# comparing case-insensitively.
#   "listen", "silent" -> True ;  "hello", "world" -> False
@quiz.question(
    "Return True if two strings are anagrams of each other (case-insensitive).",
    cases=[
        (("listen", "silent"), True),
        (("hello", "world"), False),
    ],
    answer=ANSWERS["is_anagram"],
)
def is_anagram(a, b):
    return unimplemented()


# Q3 -------------------------------------------------------------------------
# Reverse the letters of each word while keeping the words in their original
# order (split on single spaces).
#   "Python is awesome" -> "nohtyP si emosewa"
@quiz.question(
    "Reverse each word in a sentence but keep the word order.",
    cases=[
        (("Python is awesome",), "nohtyP si emosewa"),
        (("",), ""),
    ],
    answer=ANSWERS["reverse_each_word"],
)
def reverse_each_word(s):
    return unimplemented()


# Q4 -------------------------------------------------------------------------
# Check whether a sentence is a palindrome, ignoring case, spaces, and
# punctuation (only alphanumeric characters count).
#   "A man, a plan, a canal: Panama" -> True
@quiz.question(
    "Return True if a sentence is a palindrome ignoring case/spaces/punctuation.",
    cases=[
        (("A man, a plan, a canal: Panama",), True),
        (("Hello",), False),
    ],
    answer=ANSWERS["is_palindrome_sentence"],
)
def is_palindrome_sentence(s):
    return unimplemented()


# Q5 -------------------------------------------------------------------------
# Remove duplicate elements from a list while preserving the order of first
# appearance.
#   [1, 2, 2, 3, 1, 4, 2] -> [1, 2, 3, 4]
@quiz.question(
    "Remove duplicates from a list, keeping first-occurrence order.",
    cases=[
        (([1, 2, 2, 3, 1, 4, 2],), [1, 2, 3, 4]),
        (([],), []),
    ],
    answer=ANSWERS["dedupe_preserve_order"],
)
def dedupe_preserve_order(lst):
    return unimplemented()


# Q6 -------------------------------------------------------------------------
# Rotate a list to the RIGHT by n positions, returning a new list. n may be
# larger than the list length.
#   [1, 2, 3, 4, 5] rotated right by 2 -> [4, 5, 1, 2, 3]
@quiz.question(
    "Rotate a list to the right by n positions (n can exceed the length).",
    cases=[
        (([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3]),
        (([], 3), []),
    ],
    answer=ANSWERS["rotate_right"],
)
def rotate_right(lst, n):
    return unimplemented()


# Q7 -------------------------------------------------------------------------
# Using map and filter (with lambdas), return the squares of only the even
# numbers in a list.
#   [1, 2, 3, 4, 5, 6] -> [4, 16, 36]
@quiz.question(
    "Return the squares of only the even numbers, using map/filter.",
    cases=[
        (([1, 2, 3, 4, 5, 6],), [4, 16, 36]),
        (([1, 3, 5],), []),
    ],
    answer=ANSWERS["even_squares"],
)
def even_squares(nums):
    return unimplemented()


# Q8 -------------------------------------------------------------------------
# Unpack a list of positional values and a dict of keyword values into a
# function using *args/**kwargs, and summarize them as
#   (number_of_positional_args, sum_of_positional_args, sorted_keyword_items).
#   args=[1, 2, 3], kwargs={'a': 1, 'b': 2} -> (3, 6, [('a', 1), ('b', 2)])
@quiz.question(
    "Unpack args/kwargs into *args/**kwargs and return (count, sum, sorted items).",
    cases=[
        (([1, 2, 3], {"a": 1, "b": 2}), (3, 6, [("a", 1), ("b", 2)])),
        (([], {}), (0, 0, [])),
    ],
    answer=ANSWERS["summarize_args"],
)
def summarize_args(args, kwargs):
    return unimplemented()


# Q9 -------------------------------------------------------------------------
# Use the module-level `_double` decorator (which doubles a function's numeric
# result). Decorate an inner "add" function and return the doubled sum of a, b.
#   a=3, b=4 -> (3 + 4) * 2 = 14
@quiz.question(
    "Apply the _double decorator to an inner add function and return its result.",
    cases=[
        ((3, 4), 14),
        ((0, 0), 0),
    ],
    answer=ANSWERS["decorated_add"],
)
def decorated_add(a, b):
    return unimplemented()


# Q10 ------------------------------------------------------------------------
# Given parallel lists of names and scores, use zip + enumerate to build a
# ranking: sort by score descending, then number entries from 1 as
# (rank, name) tuples.
#   ["A","B","C"], [50, 90, 70] -> [(1,'B'), (2,'C'), (3,'A')]
@quiz.question(
    "Rank names by score (descending) as (rank, name), using zip and enumerate.",
    cases=[
        ((["A", "B", "C"], [50, 90, 70]), [(1, "B"), (2, "C"), (3, "A")]),
        (([], []), []),
    ],
    answer=ANSWERS["rank_by_score"],
)
def rank_by_score(names, scores):
    return unimplemented()


if __name__ == "__main__":
    quiz.run()
