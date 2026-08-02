"""Reference answers for 15_random.py.

Kept out of the topic file so solving a question doesn't spoil it.
Shown only by `--answers` mode via ANSWERS[func_name]."""

import os, sys
import random, string


def _a_divisible_by_5(seed):
    random.seed(seed)
    return [random.randrange(100, 1000, 5) for _ in range(3)]


def _a_rand_ints(seed, a, b, count):
    random.seed(seed)
    return [random.randint(a, b) for _ in range(count)]


def _a_pick_char(seed, s):
    random.seed(seed)
    return random.choice(s)


def _a_random_string(seed, length):
    random.seed(seed)
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def _a_sample_k(seed, population, k):
    random.seed(seed)
    return random.sample(population, k)


def _a_shuffled(seed, items):
    random.seed(seed)
    lst = list(items)
    random.shuffle(lst)
    return lst


def _a_rand_uniform(seed, a, b):
    random.seed(seed)
    return round(random.uniform(a, b), 6)


def _a_rand_float(seed):
    random.seed(seed)
    return round(random.random(), 6)


def _a_roll_dice(seed, times):
    random.seed(seed)
    return [random.choice([1, 2, 3, 4, 5, 6]) for _ in range(times)]


def _a_rand_range_step(seed, start, stop, step, count):
    random.seed(seed)
    return [random.randrange(start, stop, step) for _ in range(count)]


ANSWERS = {
    "divisible_by_5": _a_divisible_by_5,
    "rand_ints": _a_rand_ints,
    "pick_char": _a_pick_char,
    "random_string": _a_random_string,
    "sample_k": _a_sample_k,
    "shuffled": _a_shuffled,
    "rand_uniform": _a_rand_uniform,
    "rand_float": _a_rand_float,
    "roll_dice": _a_roll_dice,
    "rand_range_step": _a_rand_range_step,
}
