"""
Topic: Collections Module (Counter, defaultdict, OrderedDict, namedtuple, deque, ChainMap)
Source: https://pynative.com/python-collections-module-exercises/

Fill in each function body (replace `unimplemented()`), then run:
    python topics/06_collections_module.py            # grade your solutions
    python topics/06_collections_module.py --answers  # show the answer key
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from harness import Quiz, unimplemented
from answers.a06_collections_module import ANSWERS
from collections import Counter, defaultdict, OrderedDict, namedtuple, deque, ChainMap

quiz = Quiz("Collections Module")


# Q1 -------------------------------------------------------------------------
# Count how often each word appears in a sentence, ignoring case. Return a
# mapping of word -> count (a Counter compares equal to a plain dict).
#   "the cat sat on the mat the cat sat"
#   -> {'the': 3, 'cat': 2, 'sat': 2, 'on': 1, 'mat': 1}
@quiz.question(
    "Count word frequency in a sentence (case-insensitive) with Counter.",
    cases=[
        (("the cat sat on the mat the cat sat",),
         {'the': 3, 'cat': 2, 'sat': 2, 'on': 1, 'mat': 1}),
        (("",), {}),
    ],
    answer=ANSWERS["word_frequency"],
)
def word_frequency(sentence):
    return unimplemented()


# Q2 -------------------------------------------------------------------------
# Return the `n` most common items as a list of (item, count) tuples, ordered
# from most to least frequent (this is exactly Counter.most_common).
#   (["a","b","a","c","b","a"], 2) -> [('a', 3), ('b', 2)]
@quiz.question(
    "Return the n most common items as (item, count) tuples via most_common.",
    cases=[
        ((["apple", "banana", "apple", "cherry", "banana", "apple",
           "date", "cherry", "banana", "apple"], 3),
         [('apple', 4), ('banana', 3), ('cherry', 2)]),
        ((["x", "y", "x"], 0), []),
    ],
    answer=ANSWERS["top_n_common"],
)
def top_n_common(items, n):
    return unimplemented()


# Q3 -------------------------------------------------------------------------
# Given a stock list and a sold list, return the remaining stock as a mapping.
# Counter subtraction keeps only items with a positive count.
#   stock=["apple","apple","apple","banana","banana","cherry"]
#   sold =["apple","apple","banana","cherry","cherry"]
#   -> {'apple': 1, 'banana': 1}
@quiz.question(
    "Subtract a 'sold' Counter from a 'stock' Counter (positive counts only).",
    cases=[
        ((["apple", "apple", "apple", "banana", "banana", "cherry"],
          ["apple", "apple", "banana", "cherry", "cherry"]),
         {'apple': 1, 'banana': 1}),
        ((["a"], ["a", "a"]), {}),
    ],
    answer=ANSWERS["remaining_stock"],
)
def remaining_stock(stock, sold):
    return unimplemented()


# Q4 -------------------------------------------------------------------------
# Group words by their (lower-cased) first letter using defaultdict(list),
# preserving the order words are seen within each group.
#   ["apple","avocado","banana"] -> {'a': ['apple','avocado'], 'b': ['banana']}
@quiz.question(
    "Group words by their first letter with defaultdict(list).",
    cases=[
        ((["apple", "avocado", "banana", "blueberry",
           "cherry", "apricot", "cranberry", "bluebell"],),
         {'a': ['apple', 'avocado', 'apricot'],
          'b': ['banana', 'blueberry', 'bluebell'],
          'c': ['cherry', 'cranberry']}),
        (([],), {}),
    ],
    answer=ANSWERS["group_by_first_letter"],
)
def group_by_first_letter(words):
    return unimplemented()


# Q5 -------------------------------------------------------------------------
# Build a graph adjacency list from a list of directed (src, dst) edge pairs
# using defaultdict(list). Each source maps to the list of its destinations.
#   [("A","B"),("A","C"),("B","D")] -> {'A': ['B','C'], 'B': ['D']}
@quiz.question(
    "Build an adjacency list from directed edges with defaultdict(list).",
    cases=[
        (([("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")],),
         {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': ['E']}),
        (([],), {}),
    ],
    answer=ANSWERS["adjacency_list"],
)
def adjacency_list(edges):
    return unimplemented()


# Q6 -------------------------------------------------------------------------
# Given (key, value) pairs, return the keys in REVERSE insertion order. Build
# an OrderedDict and iterate it backwards.
#   [("step_1","a"),("step_2","b"),("step_3","c")] -> ['step_3','step_2','step_1']
@quiz.question(
    "Return the keys of an OrderedDict in reverse insertion order.",
    cases=[
        (([("step_1", "Load"), ("step_2", "Clean"), ("step_3", "Analyse"),
           ("step_4", "Visualise"), ("step_5", "Export")],),
         ['step_5', 'step_4', 'step_3', 'step_2', 'step_1']),
        (([("only", 1)],), ['only']),
    ],
    answer=ANSWERS["reverse_keys"],
)
def reverse_keys(pairs):
    return unimplemented()


# Q7 -------------------------------------------------------------------------
# Define a Product namedtuple(name, category, price, in_stock), build an
# instance from the arguments, and return it as a dict using _asdict().
#   ("Laptop","Electronics",999.99,True)
#   -> {'name':'Laptop','category':'Electronics','price':999.99,'in_stock':True}
@quiz.question(
    "Build a Product namedtuple and convert it to a dict with _asdict().",
    cases=[
        (("Laptop", "Electronics", 999.99, True),
         {'name': 'Laptop', 'category': 'Electronics', 'price': 999.99, 'in_stock': True}),
        (("Pen", "Office", 1.5, False),
         {'name': 'Pen', 'category': 'Office', 'price': 1.5, 'in_stock': False}),
    ],
    answer=ANSWERS["product_to_dict"],
)
def product_to_dict(name, category, price, in_stock):
    return unimplemented()


# Q8 -------------------------------------------------------------------------
# Define a Listing namedtuple(title, price, available, rating). Build one, then
# use _replace() to change only the price, and return the result as a plain
# tuple (title, new_price, available, rating).
#   ("Headphones",79.99,True,4.3, 59.99) -> ('Headphones',59.99,True,4.3)
@quiz.question(
    "Use namedtuple._replace() to change the price, returned as a tuple.",
    cases=[
        (("Wireless Headphones", 79.99, True, 4.3, 59.99),
         ('Wireless Headphones', 59.99, True, 4.3)),
        (("Mug", 10.0, True, 5.0, 8.0),
         ('Mug', 8.0, True, 5.0)),
    ],
    answer=ANSWERS["replace_price"],
)
def replace_price(title, price, available, rating, new_price):
    return unimplemented()


# Q9 -------------------------------------------------------------------------
# Rotate a sequence using a deque and return the result as a list. A positive
# n rotates right (items move toward the end's front); a negative n rotates
# left.  ([1,2,3,4,5], 2) -> [4,5,1,2,3]   ([1,2,3,4,5], -2) -> [3,4,5,1,2]
@quiz.question(
    "Rotate a sequence with deque.rotate(n) and return it as a list.",
    cases=[
        ((["Design", "Develop", "Test", "Review", "Deploy"], 2),
         ['Review', 'Deploy', 'Design', 'Develop', 'Test']),
        ((["Design", "Develop", "Test", "Review", "Deploy"], -2),
         ['Test', 'Review', 'Deploy', 'Design', 'Develop']),
    ],
    answer=ANSWERS["rotate_deque"],
)
def rotate_deque(items, n):
    return unimplemented()


# Q10 ------------------------------------------------------------------------
# Look up a key across two dictionaries using ChainMap(first, second). The
# FIRST mapping wins on conflict; if absent there, the second is used.
#   ({'a':1,'b':2}, {'b':3,'c':4}, 'b') -> 2
#   ({'a':1},       {'c':4},       'c') -> 4
@quiz.question(
    "Look up a key across two dicts with ChainMap (first dict wins).",
    cases=[
        (({'a': 1, 'b': 2}, {'b': 3, 'c': 4}, 'b'), 2),
        (({'a': 1}, {'c': 4}, 'c'), 4),
    ],
    answer=ANSWERS["chainmap_lookup"],
)
def chainmap_lookup(first, second, key):
    return unimplemented()


if __name__ == "__main__":
    quiz.run()
