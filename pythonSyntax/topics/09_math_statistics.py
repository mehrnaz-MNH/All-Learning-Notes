"""
Topic: Math and Statistics
Source: https://pynative.com/python-math-statistics-exercises/

Fill in each function body (replace `unimplemented()`), then run:
    python topics/09_math_statistics.py            # grade your solutions
    python topics/09_math_statistics.py --answers  # show the answer key
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from harness import Quiz, unimplemented
from answers.a09_math_statistics import ANSWERS

import math, statistics

quiz = Quiz("Math and Statistics")

# A tolerant float comparison so tiny rounding differences never fail a case.
close = lambda g, e: abs(g - e) < 1e-6
# Same idea but for a pair (tuple) of floats.
close2 = lambda g, e: all(abs(a - b) < 1e-6 for a, b in zip(g, e))


# Q1 -------------------------------------------------------------------------
# Return the (real) square root of a non-negative number using math.sqrt.
# The result is always a float.
#   n=144 -> 12.0     n=0 -> 0.0
@quiz.question(
    "Return the square root of n as a float (math.sqrt).",
    cases=[
        ((144,), 12.0),
        ((0,), 0.0),
    ],
    answer=ANSWERS["square_root"],
    compare=close,
)
def square_root(n):
    return unimplemented()


# Q2 -------------------------------------------------------------------------
# Raise base to the power exp using math.pow, which always returns a float.
#   base=2, exp=10 -> 1024.0
#   base=2, exp=-1 -> 0.5   (negative exponent gives a fraction)
@quiz.question(
    "Return base raised to exp as a float (math.pow).",
    cases=[
        ((2, 10), 1024.0),
        ((2, -1), 0.5),
    ],
    answer=ANSWERS["power"],
    compare=close,
)
def power(base, exp):
    return unimplemented()


# Q3 -------------------------------------------------------------------------
# Return n! (n factorial) using math.factorial. This is an exact integer.
#   n=10 -> 3628800     n=0 -> 1  (0! is defined as 1)
@quiz.question(
    "Return the factorial of n (math.factorial).",
    cases=[
        ((10,), 3628800),
        ((0,), 1),
    ],
    answer=ANSWERS["factorial"],
)
def factorial(n):
    return unimplemented()


# Q4 -------------------------------------------------------------------------
# Return the greatest common divisor of two integers using math.gcd.
#   a=48, b=180 -> 12
#   a=13, b=7   -> 1   (coprime numbers share only the divisor 1)
@quiz.question(
    "Return the greatest common divisor of a and b (math.gcd).",
    cases=[
        ((48, 180), 12),
        ((13, 7), 1),
    ],
    answer=ANSWERS["gcd"],
)
def gcd(a, b):
    return unimplemented()


# Q5 -------------------------------------------------------------------------
# Return a (ceiling, floor) pair for x using math.ceil and math.floor.
# Ceiling rounds up toward +inf, floor rounds down toward -inf.
#   x=4.7  -> (5, 4)
#   x=-4.7 -> (-4, -5)   (note how negatives round the "other" way)
@quiz.question(
    "Return (ceil(x), floor(x)) as a tuple of ints.",
    cases=[
        ((4.7,), (5, 4)),
        ((-4.7,), (-4, -5)),
    ],
    answer=ANSWERS["ceil_and_floor"],
)
def ceil_and_floor(x):
    return unimplemented()


# Q6 -------------------------------------------------------------------------
# Return the natural logarithm (base e) of x using math.log.
#   x=1000 -> 6.907755278982137
#   x=1    -> 0.0   (ln(1) is always 0)
@quiz.question(
    "Return the natural log (base e) of x (math.log).",
    cases=[
        ((1000,), 6.907755278982137),
        ((1,), 0.0),
    ],
    answer=ANSWERS["natural_log"],
    compare=close,
)
def natural_log(x):
    return unimplemented()


# Q7 -------------------------------------------------------------------------
# Return the arithmetic mean (average) of a list of numbers using
# statistics.mean.
#   data=[10,20,30,40] -> 25.0
#   data=[5,5,5]       -> 5.0
@quiz.question(
    "Return the mean (average) of the numbers (statistics.mean).",
    cases=[
        (([10, 20, 30, 40],), 25.0),
        (([5, 5, 5],), 5.0),
    ],
    answer=ANSWERS["mean"],
    compare=close,
)
def mean(data):
    return unimplemented()


# Q8 -------------------------------------------------------------------------
# Return the median (middle value) of a list using statistics.median.
# For an even count it returns the average of the two middle values.
#   data=[1,2,3,4] -> 2.5
#   data=[1,2,3]   -> 2      (odd count returns the exact middle)
@quiz.question(
    "Return the median (middle value) of the numbers (statistics.median).",
    cases=[
        (([1, 2, 3, 4],), 2.5),
        (([1, 2, 3],), 2),
    ],
    answer=ANSWERS["median"],
    compare=close,
)
def median(data):
    return unimplemented()


# Q9 -------------------------------------------------------------------------
# Return the mode (most frequently occurring value) using statistics.mode.
#   data=[1,2,2,3,3,3] -> 3
#   data=[7,7]         -> 7
@quiz.question(
    "Return the mode (most common value) of the numbers (statistics.mode).",
    cases=[
        (([1, 2, 2, 3, 3, 3],), 3),
        (([7, 7],), 7),
    ],
    answer=ANSWERS["mode"],
)
def mode(data):
    return unimplemented()


# Q10 ------------------------------------------------------------------------
# Return a (stdev, variance) pair for the SAMPLE using statistics.stdev and
# statistics.variance. Variance measures spread; stdev is its square root.
#   data=[2,4,4,4,5,5,7,9] -> (2.138089935299395, 4.571428571428571)
#   data=[1,2,3,4,5]       -> (1.5811388300841898, 2.5)
@quiz.question(
    "Return (sample stdev, sample variance) as a tuple of floats.",
    cases=[
        (([2, 4, 4, 4, 5, 5, 7, 9],), (2.138089935299395, 4.571428571428571)),
        (([1, 2, 3, 4, 5],), (1.5811388300841898, 2.5)),
    ],
    answer=ANSWERS["stdev_and_variance"],
    compare=close2,
)
def stdev_and_variance(data):
    return unimplemented()


if __name__ == "__main__":
    quiz.run()
