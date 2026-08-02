"""
Topic: Random Numbers (the `random` module)
Source: https://pynative.com/python-random-number-generation-exercise-questions-and-challenge/

Fill in each function body (replace `unimplemented()`), then run:
    python topics/15_random.py            # grade your solutions
    python topics/15_random.py --answers  # show the answer key

IMPORTANT: every function is DETERMINISTIC. Each one takes a `seed` argument
and MUST call `random.seed(seed)` as its very first line, before any other
random call. Seeding the generator makes the sequence of "random" values
reproducible, so the same seed always produces the same output -- which is
what lets these exercises have fixed expected answers.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from harness import Quiz, unimplemented
from answers.a15_random import ANSWERS
import random, string

quiz = Quiz("Random Numbers")


# Q1 -------------------------------------------------------------------------
# Return a list of 3 random integers between 100 and 999 (inclusive) that are
# each divisible by 5. Use random.randrange(100, 1000, 5) three times.
#   seed=0 -> [590, 635, 150]
# Seeding first makes the result reproducible for a given seed.
@quiz.question(
    "Return 3 random ints in [100,999] divisible by 5 (reproducible for a seed).",
    cases=[
        ((0,), [590, 635, 150]),
        ((42,), [915, 240, 130]),
    ],
    answer=ANSWERS["divisible_by_5"],
)
def divisible_by_5(seed):
    return unimplemented()


# Q2 -------------------------------------------------------------------------
# Return a list of `count` random integers between a and b (inclusive), using
# random.randint(a, b). randint includes BOTH endpoints.
#   seed=0, a=1, b=10, count=3 -> [7, 7, 1]
# Seeding first makes the result reproducible for a given seed.
@quiz.question(
    "Return `count` random ints in [a,b] inclusive (reproducible for a seed).",
    cases=[
        ((0, 1, 10, 3), [7, 7, 1]),
        ((5, 1, 6, 2), [5, 3]),
    ],
    answer=ANSWERS["rand_ints"],
)
def rand_ints(seed, a, b, count):
    return unimplemented()


# Q3 -------------------------------------------------------------------------
# Return a single random character picked from string `s` using
# random.choice(s).
#   seed=0, s='pynative' -> 'v'
# Seeding first makes the pick reproducible for a given seed.
@quiz.question(
    "Pick one random character from a string (reproducible for a seed).",
    cases=[
        ((0, 'pynative'), 'v'),
        ((3, 'pynative'), 'a'),
    ],
    answer=ANSWERS["pick_char"],
)
def pick_char(seed, s):
    return unimplemented()


# Q4 -------------------------------------------------------------------------
# Build a random string of the given length using only letters (both cases).
# Pick each character with random.choice(string.ascii_letters).
#   seed=0, length=5 -> 'yWAcq'
# Seeding first makes the string reproducible for a given seed.
@quiz.question(
    "Build a random letters-only string of a given length (reproducible for a seed).",
    cases=[
        ((0, 5), 'yWAcq'),
        ((7, 3), 'ujz'),
    ],
    answer=ANSWERS["random_string"],
)
def random_string(seed, length):
    return unimplemented()


# Q5 -------------------------------------------------------------------------
# Return `k` unique elements chosen from `population` using random.sample.
# Unlike choice, sample never repeats an element.
#   seed=0, population=[10,20,30,40,50], k=3 -> [40, 50, 10]
# Seeding first makes the selection reproducible for a given seed.
@quiz.question(
    "Pick `k` unique elements from a list with random.sample (reproducible for a seed).",
    cases=[
        ((0, [10, 20, 30, 40, 50], 3), [40, 50, 10]),
        ((2, [1, 2, 3, 4], 2), [1, 4]),
    ],
    answer=ANSWERS["sample_k"],
)
def sample_k(seed, population, k):
    return unimplemented()


# Q6 -------------------------------------------------------------------------
# Return a shuffled COPY of `items` (do not mutate the input). Copy the list,
# then use random.shuffle on the copy and return it.
#   seed=0, items=[1,2,3,4,5] -> [3, 2, 1, 5, 4]
# Seeding first makes the shuffle order reproducible for a given seed.
@quiz.question(
    "Return a shuffled copy of a list (reproducible for a seed).",
    cases=[
        ((0, [1, 2, 3, 4, 5]), [3, 2, 1, 5, 4]),
        ((9, ['a', 'b', 'c']), ['a', 'c', 'b']),
    ],
    answer=ANSWERS["shuffled"],
)
def shuffled(seed, items):
    return unimplemented()


# Q7 -------------------------------------------------------------------------
# Return a random float in [a, b] using random.uniform(a, b), rounded to 6
# decimal places.
#   seed=0, a=1.0, b=10.0 -> 8.599797
# Seeding first makes the float reproducible for a given seed.
@quiz.question(
    "Return a random float in [a,b] via random.uniform, rounded to 6 dp (reproducible).",
    cases=[
        ((0, 1.0, 10.0), 8.599797),
        ((4, 0.0, 1.0), 0.236048),
    ],
    answer=ANSWERS["rand_uniform"],
)
def rand_uniform(seed, a, b):
    return unimplemented()


# Q8 -------------------------------------------------------------------------
# Return a random float in [0.0, 1.0) using random.random(), rounded to 6
# decimal places.
#   seed=0 -> 0.844422
# Seeding first makes the float reproducible for a given seed.
@quiz.question(
    "Return random.random() in [0,1) rounded to 6 dp (reproducible for a seed).",
    cases=[
        ((0,), 0.844422),
        ((100,), 0.145669),
    ],
    answer=ANSWERS["rand_float"],
)
def rand_float(seed):
    return unimplemented()


# Q9 -------------------------------------------------------------------------
# Simulate rolling a 6-sided die `times` times, returning the list of results.
# Pick each roll with random.choice([1,2,3,4,5,6]).
#   seed=0, times=5 -> [4, 4, 1, 3, 5]
# Seeding first makes the rolls reproducible for a given seed.
@quiz.question(
    "Roll a 6-sided die `times` times, returning the results (reproducible for a seed).",
    cases=[
        ((0, 5), [4, 4, 1, 3, 5]),
        ((1, 3), [2, 5, 1]),
    ],
    answer=ANSWERS["roll_dice"],
)
def roll_dice(seed, times):
    return unimplemented()


# Q10 ------------------------------------------------------------------------
# Return a list of `count` random values from range(start, stop, step) using
# random.randrange(start, stop, step). randrange excludes `stop` and only
# yields values reachable by the step.
#   seed=0, start=100, stop=1000, step=5, count=3 -> [590, 635, 150]
# Seeding first makes the values reproducible for a given seed.
@quiz.question(
    "Return `count` values from randrange(start, stop, step) (reproducible for a seed).",
    cases=[
        ((0, 100, 1000, 5, 3), [590, 635, 150]),
        ((11, 0, 50, 10, 4), [30, 40, 30, 30]),
    ],
    answer=ANSWERS["rand_range_step"],
)
def rand_range_step(seed, start, stop, step, count):
    return unimplemented()


if __name__ == "__main__":
    quiz.run()
