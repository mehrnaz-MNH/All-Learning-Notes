"""Reference answers for 09_math_statistics.py.

Kept out of the topic file so solving a question doesn't spoil it.
Shown only by `--answers` mode via ANSWERS[func_name]."""

import os, sys
import math, statistics


ANSWERS = {
    "square_root": lambda n: math.sqrt(n),
    "power": lambda base, exp: math.pow(base, exp),
    "factorial": lambda n: math.factorial(n),
    "gcd": lambda a, b: math.gcd(a, b),
    "ceil_and_floor": lambda x: (math.ceil(x), math.floor(x)),
    "natural_log": lambda x: math.log(x),
    "mean": lambda data: statistics.mean(data),
    "median": lambda data: statistics.median(data),
    "mode": lambda data: statistics.mode(data),
    "stdev_and_variance": lambda data: (statistics.stdev(data), statistics.variance(data)),
}
