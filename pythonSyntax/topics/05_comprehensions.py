"""
Topic: Comprehensions
Source: https://pynative.com/python-comprehensions-exercises/

Fill in each function body (replace `unimplemented()`), then run:
    python topics/05_comprehensions.py            # grade your solutions
    python topics/05_comprehensions.py --answers  # show the answer key
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from harness import Quiz, unimplemented
from answers.a05_comprehensions import ANSWERS

quiz = Quiz("Comprehensions")


# Q1 -------------------------------------------------------------------------
# Use a list comprehension to return the squares of the integers 1..n
# (inclusive).
#   n=5 -> [1, 4, 9, 16, 25]
@quiz.question(
    "Return a list of squares for the integers 1..n using a list comprehension.",
    cases=[
        ((5,), [1, 4, 9, 16, 25]),
        ((1,), [1]),
        ((0,), []),
    ],
    answer=ANSWERS["squares"],
)
def squares(n):
    return unimplemented()


# Q2 -------------------------------------------------------------------------
# Use a list comprehension to keep ONLY the even numbers from a list, in the
# original order.
#   [3, 7, 2, 14, 9, 8] -> [2, 14, 8]
@quiz.question(
    "Filter a list down to only its even numbers (keep original order).",
    cases=[
        (([3, 7, 2, 14, 9, 8, 11, 6, 5, 10],), [2, 14, 8, 6, 10]),
        (([1, 3, 5],), []),
    ],
    answer=ANSWERS["only_evens"],
)
def only_evens(nums):
    return unimplemented()


# Q3 -------------------------------------------------------------------------
# Flatten a 2D list (list of lists) into a single flat list, preserving order.
# This uses two `for` clauses in one comprehension.
#   [[1, 2, 3], [4, 5], [6, 7, 8]] -> [1, 2, 3, 4, 5, 6, 7, 8]
@quiz.question(
    "Flatten a list of lists into a single list using nested for-clauses.",
    cases=[
        (([[1, 2, 3], [4, 5], [6, 7, 8, 9]],), [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        (([[], [1], []],), [1]),
    ],
    answer=ANSWERS["flatten"],
)
def flatten(matrix):
    return unimplemented()


# Q4 -------------------------------------------------------------------------
# In a single comprehension, filter to the ODD numbers and then square them.
#   [1, 2, 3, 4, 5] -> [1, 9, 25]   (squares of 1, 3, 5)
@quiz.question(
    "Square only the odd numbers of a list, in one comprehension (filter + transform).",
    cases=[
        (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],), [1, 9, 25, 49, 81]),
        (([2, 4, 6],), []),
    ],
    answer=ANSWERS["squares_of_odds"],
)
def squares_of_odds(nums):
    return unimplemented()


# Q5 -------------------------------------------------------------------------
# Use a dict comprehension to count how many times each word appears in a list.
#   ["apple", "banana", "apple"] -> {"apple": 2, "banana": 1}
@quiz.question(
    "Build a {word: count} frequency dictionary from a list of words.",
    cases=[
        ((["apple", "banana", "apple", "cherry", "banana", "apple", "date"],),
         {"apple": 3, "banana": 2, "cherry": 1, "date": 1}),
        (([],), {}),
    ],
    answer=ANSWERS["word_frequency"],
)
def word_frequency(words):
    return unimplemented()


# Q6 -------------------------------------------------------------------------
# Use a dict comprehension to keep only the entries whose value is >= 50.
#   {"Alice": 82, "Bob": 45, "Eve": 55} -> {"Alice": 82, "Eve": 55}
@quiz.question(
    "Keep only the dict entries whose value is at least 50 (filter a dict).",
    cases=[
        (({"Alice": 82, "Bob": 45, "Charlie": 91, "Diana": 37, "Eve": 55, "Frank": 49},),
         {"Alice": 82, "Charlie": 91, "Eve": 55}),
        (({"a": 10, "b": 20},), {}),
    ],
    answer=ANSWERS["passing_scores"],
)
def passing_scores(scores):
    return unimplemented()


# Q7 -------------------------------------------------------------------------
# Use a set comprehension to collect the distinct vowels that appear in a
# string. Return a set (order does not matter).
#   "hello world" -> {"o", "e"}
@quiz.question(
    "Return the set of distinct vowels (a, e, i, o, u) found in a string.",
    cases=[
        (("the quick brown fox jumps over the lazy dog",), {"a", "e", "i", "o", "u"}),
        (("rhythm",), set()),
    ],
    answer=ANSWERS["unique_vowels"],
)
def unique_vowels(s):
    return unimplemented()


# Q8 -------------------------------------------------------------------------
# Use a set comprehension to find the elements that appear in BOTH lists
# (the intersection). Return a set.
#   [1, 2, 3, 2] and [3, 4, 2] -> {2, 3}
@quiz.question(
    "Return the set of elements present in both input lists (intersection).",
    cases=[
        (([1, 2, 3, 4, 5, 3, 2], [3, 4, 5, 6, 7, 4, 5]), {3, 4, 5}),
        (([1, 2], [3, 4]), set()),
    ],
    answer=ANSWERS["common_elements"],
)
def common_elements(a, b):
    return unimplemented()


# Q9 -------------------------------------------------------------------------
# Transpose a matrix (swap rows and columns) using a nested list comprehension.
# Assume the matrix is rectangular (every row is the same length).
#   [[1, 2, 3], [4, 5, 6]] -> [[1, 4], [2, 5], [3, 6]]
@quiz.question(
    "Transpose a rectangular matrix using a nested list comprehension.",
    cases=[
        (([[1, 2, 3], [4, 5, 6], [7, 8, 9]],), [[1, 4, 7], [2, 5, 8], [3, 6, 9]]),
        (([[1, 2, 3], [4, 5, 6]],), [[1, 4], [2, 5], [3, 6]]),
    ],
    answer=ANSWERS["transpose"],
)
def transpose(m):
    return unimplemented()


# Q10 ------------------------------------------------------------------------
# Build the Cartesian product of two lists as a list of (x, y) tuples, using
# two for-clauses. The first list varies slowest.
#   [1, 2] and ["a", "b"] -> [(1, "a"), (1, "b"), (2, "a"), (2, "b")]
@quiz.question(
    "Return the Cartesian product of two lists as a list of (x, y) tuples.",
    cases=[
        (([1, 2, 3], ["a", "b", "c"]),
         [(1, "a"), (1, "b"), (1, "c"),
          (2, "a"), (2, "b"), (2, "c"),
          (3, "a"), (3, "b"), (3, "c")]),
        (([1, 2], []), []),
    ],
    answer=ANSWERS["cartesian_product"],
)
def cartesian_product(xs, ys):
    return unimplemented()


if __name__ == "__main__":
    quiz.run()
