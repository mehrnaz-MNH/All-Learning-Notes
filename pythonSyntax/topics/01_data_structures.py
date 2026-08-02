"""
Topic: Data Structures
Source: https://pynative.com/python-data-structure-exercise-for-beginners/

Fill in each function body (replace `unimplemented()`), then run:
    python topics/01_data_structures.py            # grade your solutions
    python topics/01_data_structures.py --answers  # show the answer key
"""
from collections import defaultdict
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from harness import Quiz, unimplemented
from answers.a01_data_structures import ANSWERS

quiz = Quiz("Data Structures")


# Q1 -------------------------------------------------------------------------
# Build a new list from the odd-indexed elements of the first list followed
# by the even-indexed elements of the second list.
#   l1=[3,6,9,12,15,18,21], l2=[4,8,12,16,20,24,28]
#   -> [6, 12, 18, 4, 12, 20, 28]
@quiz.question(
    "New list = odd-indexed items of list1 + even-indexed items of list2.",
    cases=[
        (([3, 6, 9, 12, 15, 18, 21], [4, 8, 12, 16, 20, 24, 28]),
         [6, 12, 18, 4, 12, 20, 28]),
        (([1, 2], [9, 8]), [2, 9]),
    ],
    answer=ANSWERS["mix_indexed"],
)
def mix_indexed(l1, l2):

    return l1[1::2] + l2[0::2]


# Q2 -------------------------------------------------------------------------
# Slice a list into three equal chunks and reverse the order of each chunk.
# Return a list of the three reversed chunks.
#   [11,45,8,23,14,12,78,45,89]
#   -> [[8,45,11], [12,14,23], [89,45,78]]
@quiz.question(
    "Split a list into 3 equal chunks and reverse each chunk.",
    cases=[
        (([11, 45, 8, 23, 14, 12, 78, 45, 89],),
         [[8, 45, 11], [12, 14, 23], [89, 45, 78]]),
        (([1, 2, 3],), [[1], [2], [3]]),
    ],
    answer=ANSWERS["reverse_chunks"],
)
def reverse_chunks(lst):
    c_l = len(lst) // 3
    chunks = [lst[0:c_l] , lst[c_l:c_l*2] , lst[c_l*2:]]
    return [chunk[::-1] for chunk in chunks]


# Q3 -------------------------------------------------------------------------
# Count how many times each element occurs in a list, returned as a dict
# mapping element -> count (in first-seen order).
#   [11,45,8,11,23,45,23,45,89] -> {11:2, 45:3, 8:1, 23:2, 89:1}
@quiz.question(
    "Count the occurrences of each element in a list, returning a dict.",
    cases=[
        (([11, 45, 8, 11, 23, 45, 23, 45, 89],),
         {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}),
        (([],), {}),
    ],
    answer=ANSWERS["count_elements"],
)
def count_elements(lst):
    count_dict = defaultdict(int)
    for item in lst:
        count_dict[item] += 1
    return count_dict


# Q4 -------------------------------------------------------------------------
# Pair up corresponding elements of two lists into a set of tuples.
#   [2,3,4], [4,9,16] -> {(2,4), (3,9), (4,16)}
@quiz.question(
    "Pair corresponding elements of two lists into a set of tuples.",
    cases=[
        (([2, 3, 4, 5, 6, 7, 8], [4, 9, 16, 25, 36, 49, 64]),
         {(2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64)}),
        (([1], [2]), {(1, 2)}),
    ],
    answer=ANSWERS["paired_set"],
)
def paired_set(a, b):
    pair_set = set()
    # for i in range(len(a)):
    #     pair_set.add((a[i],b[i]))
    for x,y in zip(a,b):
        pair_set.add((x,y))
    return pair_set


# Q5 -------------------------------------------------------------------------
# Return the set of elements common to both sets (their intersection).
#   {23,42,65,57,78,83,29} & {57,83,29,67,73,43,48} -> {57, 83, 29}
@quiz.question(
    "Return the intersection (common elements) of two sets.",
    cases=[
        (({23, 42, 65, 57, 78, 83, 29}, {57, 83, 29, 67, 73, 43, 48}),
         {57, 83, 29}),
        (({1, 2}, {3, 4}), set()),
    ],
    answer=ANSWERS["common_elements"],
)
def common_elements(a, b):
    return a & b


# Q6 -------------------------------------------------------------------------
# Return True if the first set is a subset of the second set.
#   {27,43,34} subset of {34,93,22,27,43,53,48} -> True
@quiz.question(
    "Return True if the first set is a subset of the second set.",
    cases=[
        (({27, 43, 34}, {34, 93, 22, 27, 43, 53, 48}), True),
        (({1, 9}, {1, 2, 3}), False),
    ],
    answer=ANSWERS["is_subset"],
)
def is_subset(a, b):
    #return a <= b
    return a.issubset(b)


# Q7 -------------------------------------------------------------------------
# Keep only the list elements that appear as a value in the dictionary.
#   [47,64,69,37,76,83,95,97], {'Jhon':47,'Emma':69,'Kelly':76,'Jason':97}
#   -> [47, 69, 76, 97]
@quiz.question(
    "Filter a list, keeping only items present among a dict's values.",
    cases=[
        (([47, 64, 69, 37, 76, 83, 95, 97],
          {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}),
         [47, 69, 76, 97]),
        (([1, 2, 3], {'a': 2}), [2]),
    ],
    answer=ANSWERS["filter_by_values"],
)
def filter_by_values(lst, d):
    value_set = {val for val in d.values()}
    inter_res = set(lst) & value_set
    return list(inter_res)


# Q8 -------------------------------------------------------------------------
# Return the dictionary's values with duplicates removed, as a list in
# first-seen order.
#   {'jan':47,'feb':52,'march':47,'April':44,'May':52,'June':53,'July':54}
#   -> [47, 52, 44, 53, 54]
@quiz.question(
    "Return a dict's values as a list with duplicates removed (in order).",
    cases=[
        (({'jan': 47, 'feb': 52, 'march': 47, 'April': 44,
           'May': 52, 'June': 53, 'July': 54},),
         [47, 52, 44, 53, 54]),
        (({},), []),
    ],
    answer=ANSWERS["unique_values"],
)
def unique_values(d):

    return list(dict.fromkeys(d.values()))


# Q9 -------------------------------------------------------------------------
# Remove duplicates from a list (keeping first-seen order) and return the
# result as a tuple.
#   [87,45,41,65,94,41,99,94] -> (87, 45, 41, 65, 94, 99)
@quiz.question(
    "Remove duplicates from a list (keep order) and return a tuple.",
    cases=[
        (([87, 45, 41, 65, 94, 41, 99, 94],), (87, 45, 41, 65, 94, 99)),
        (([1, 1, 1],), (1,)),
    ],
    answer=ANSWERS["unique_tuple"],
)
def unique_tuple(lst):
    return tuple(dict.fromkeys(lst))


# Q10 ------------------------------------------------------------------------
# Given a list of numbers, return a tuple (minimum, maximum).
#   [87,45,41,65,99] -> (41, 99)
@quiz.question(
    "Return (min, max) of a list of numbers as a tuple.",
    cases=[
        (([87, 45, 41, 65, 99],), (41, 99)),
        (([5],), (5, 5)),
    ],
    answer=ANSWERS["min_max"],
)
def min_max(lst):
    # find min
    lst_min = float('inf')
    for item in lst :
        lst_min = min(lst_min , item)
    # find max
    lst_max = float('-inf')
    for item in lst :
        lst_max = max(lst_max , item)
    # return tuple
    return (lst_min , lst_max)


if __name__ == "__main__":
    quiz.run()
