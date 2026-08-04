"""
Topic: Dictionaries
Source: https://pynative.com/python-dictionary-exercise-with-solutions/

Fill in each function body (replace `unimplemented()`), then run:
    python topics/02_dictionaries.py            # grade your solutions
    python topics/02_dictionaries.py --answers  # show the answer key
"""
from collections import defaultdict
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from harness import Quiz, unimplemented
from answers.a02_dictionaries import ANSWERS
from functools import reduce

quiz = Quiz("Dictionaries")


# Q1 -------------------------------------------------------------------------
# Given two lists (keys and values), build a single dictionary mapping each
# key to the value at the same position.
#   keys=['Ten','Twenty','Thirty'], values=[10,20,30]
#   -> {'Ten':10, 'Twenty':20, 'Thirty':30}
@quiz.question(
    "Combine two lists into a dictionary (keys[i] -> values[i]).",
    cases=[
        ((['Ten', 'Twenty', 'Thirty'], [10, 20, 30]),
         {'Ten': 10, 'Twenty': 20, 'Thirty': 30}),
        (([], []), {}),
    ],
    answer=ANSWERS["zip_to_dict"],
)
def zip_to_dict(keys, values):
    return dict(zip(keys,values))


# Q2 -------------------------------------------------------------------------
# Merge two dictionaries into one. On key conflict, the second wins.
@quiz.question(
    "Merge two dictionaries into a new one (second dict wins on conflict).",
    cases=[
        (({'a': 1, 'b': 2}, {'b': 3, 'c': 4}), {'a': 1, 'b': 3, 'c': 4}),
        (({}, {'x': 9}), {'x': 9}),
    ],
    answer=ANSWERS["merge_dicts"],
)
def merge_dicts(d1, d2):
    return d1 | d2


# Q3 -------------------------------------------------------------------------
# Return the value found at sample['key1']['key2'] in a nested dictionary.
#   {'class': {'student': {'name': 'Mike'}}}, path ('class','student','name') -> 'Mike'
@quiz.question(
    "Access a value in a nested dictionary given a tuple path of keys.",
    cases=[
        (({'class': {'student': {'name': 'Mike'}}}, ('class', 'student', 'name')), 'Mike'),
        (({'a': {'b': 5}}, ('a', 'b')), 5),
    ],
    answer=ANSWERS["nested_get"],
)
def nested_get(d, path):
    current = d
    for p in path :
        current = current[p]
    return current
    # reduce(lambda current , key : current[key] , path , d)



# Q4 -------------------------------------------------------------------------
# Build a dict {n: n*n} for n in 1..num (inclusive).  num=5 -> {1:1,2:4,3:9,4:16,5:25}
@quiz.question(
    "Create a dictionary of numbers 1..num mapped to their squares.",
    cases=[
        ((5,), {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}),
        ((1,), {1: 1}),
    ],
    answer=ANSWERS["squares_dict"],
)
def squares_dict(num):
    return { n:n*n for n in range(1 , num+1)}


# Q5 -------------------------------------------------------------------------
# Given a dict, return a new dict containing ONLY the listed keys.
@quiz.question(
    "Return a sub-dictionary keeping only the given keys.",
    cases=[
        (({'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'NY'}, ['name', 'salary']),
         {'name': 'Kelly', 'salary': 8000}),
        (({'a': 1, 'b': 2}, []), {}),
    ],
    answer=ANSWERS["pick_keys"],
)
def pick_keys(d, keys):
    return {key:value for key , value in d.items() if key in set(keys)}




# Q6 -------------------------------------------------------------------------
# Return the key that has the minimum value.
@quiz.question(
    "Return the key with the minimum value in the dictionary.",
    cases=[
        (({'a': 3, 'b': 1, 'c': 2},), 'b'),
        (({'x': 10},), 'x'),
    ],
    answer=ANSWERS["key_of_min_value"],
)
def key_of_min_value(d):
    return min(d.items() , key = lambda item:item[1])[0]


# Q7 -------------------------------------------------------------------------
# Remove a key from a dict *without raising* if the key is absent, and return
# the resulting dict (do not mutate the input).
@quiz.question(
    "Return a copy of the dict with `key` removed (no error if key is missing).",
    cases=[
        (({'a': 1, 'b': 2}, 'a'), {'b': 2}),
        (({'a': 1}, 'zzz'), {'a': 1}),
    ],
    answer=ANSWERS["drop_key"],
)
def drop_key(d, key):
    return dict(filter(lambda item: item[0] != key , d.items() ))


# Q8 -------------------------------------------------------------------------
# Count the frequency of each character in a string, returned as a dict.
@quiz.question(
    "Count character frequency in a string, returning a {char: count} dict.",
    cases=[
        (("hello",), {'h': 1, 'e': 1, 'l': 2, 'o': 1}),
        (("",), {}),
    ],
    answer=ANSWERS["char_frequency"],
)
def char_frequency(s):
      char_freq = defaultdict(int)
      for c in s :
          if c not in char_freq:
              char_freq[c] = 0
          char_freq[c] += 1
      return char_freq




# Q9 -------------------------------------------------------------------------
# Invert a dictionary: swap keys and values. Assume values are unique/hashable.
@quiz.question(
    "Invert a dictionary so values become keys and keys become values.",
    cases=[
        (({'a': 1, 'b': 2},), {1: 'a', 2: 'b'}),
        (({},), {}),
    ],
    answer=ANSWERS["invert_dict"],
)
def invert_dict(d):
    return {value : key for key , value in d.items()}


# Q10 ------------------------------------------------------------------------
# Sum all the values in a dictionary.
@quiz.question(
    "Return the sum of all values in the dictionary.",
    cases=[
        (({'a': 100, 'b': 200, 'c': 300},), 600),
        (({},), 0),
    ],
    answer=ANSWERS["sum_values"],
)
def sum_values(d):
    return reduce(lambda x , y : x + y , d.values() , 0 )


if __name__ == "__main__":
    quiz.run()
