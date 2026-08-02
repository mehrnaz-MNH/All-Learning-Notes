"""
Topic: Object-Oriented Programming (OOP)
Source: https://pynative.com/python-object-oriented-programming-oop-exercise/

Each function builds and/or uses a class INSIDE its body and RETURNS a value
that demonstrates the class works. Fill in each function body (replace
`unimplemented()`), then run:
    python topics/08_oop.py            # grade your solutions
    python topics/08_oop.py --answers  # show the answer key
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from harness import Quiz, unimplemented
from answers.a08_oop import ANSWERS

quiz = Quiz("Object-Oriented Programming")


# Q1 -------------------------------------------------------------------------
# Define a Vehicle class with a constructor (__init__) that stores two instance
# attributes, `name` and `max_speed`, and an instance method describe() that
# returns "<name> goes <max_speed>". Create a Vehicle and return describe().
#   vehicle_describe("Bus", 80)  -> "Bus goes 80"
@quiz.question(
    "Build a Vehicle class (__init__ + describe()); return '<name> goes <max_speed>'.",
    cases=[
        (("Bus", 80), "Bus goes 80"),
        (("Car", 120), "Car goes 120"),
    ],
    answer=ANSWERS["vehicle_describe"],
)
def vehicle_describe(name, max_speed):
    return unimplemented()


# Q2 -------------------------------------------------------------------------
# Define a Counter class with a CLASS variable `count` (shared by all instances)
# that starts at 0 and is incremented by 1 inside __init__ each time an object
# is created. Create `n` Counter objects, then return the class variable count.
#   count_instances(3) -> 3   (three objects were created)
@quiz.question(
    "Use a class variable to count how many instances were created; return the count.",
    cases=[
        ((3,), 3),
        ((0,), 0),
    ],
    answer=ANSWERS["count_instances"],
)
def count_instances(n):
    return unimplemented()


# Q3 -------------------------------------------------------------------------
# Define a Rectangle class storing `width` and `height` as instance attributes,
# with instance methods area() and perimeter(). Create a Rectangle and return
# the tuple (area, perimeter).
#   rectangle_stats(4, 5) -> (20, 18)   # area=4*5, perimeter=2*(4+5)
@quiz.question(
    "Build a Rectangle class with area() and perimeter(); return (area, perimeter).",
    cases=[
        ((4, 5), (20, 18)),
        ((3, 3), (9, 12)),
    ],
    answer=ANSWERS["rectangle_stats"],
)
def rectangle_stats(width, height):
    return unimplemented()


# Q4 -------------------------------------------------------------------------
# Define a BankAccount class with a `balance` instance attribute and a
# withdraw(amount) method that protects the balance: if `amount` is greater
# than the current balance it does NOTHING (rejects the withdrawal); otherwise
# it subtracts the amount. Create an account, attempt the withdrawal, and
# return the final balance.
#   withdraw_protected(100, 30)  -> 70    (allowed)
#   withdraw_protected(100, 200) -> 100   (rejected, balance unchanged)
@quiz.question(
    "Build a BankAccount whose withdraw() rejects over-withdrawals; return final balance.",
    cases=[
        ((100, 30), 70),
        ((100, 200), 100),
    ],
    answer=ANSWERS["withdraw_protected"],
)
def withdraw_protected(balance, amount):
    return unimplemented()


# Q5 -------------------------------------------------------------------------
# Define a base Vehicle class with __init__(name, max_speed). Define a Bus class
# that INHERITS from Vehicle (adds nothing new). Create a Bus and return the
# string "<name> - <max_speed>" using the inherited attributes.
#   bus_info("School Bus", 60) -> "School Bus - 60"
@quiz.question(
    "Make Bus inherit from Vehicle; return '<name> - <max_speed>' via inherited attrs.",
    cases=[
        (("School Bus", 60), "School Bus - 60"),
        (("Mini", 40), "Mini - 40"),
    ],
    answer=ANSWERS["bus_info"],
)
def bus_info(name, max_speed):
    return unimplemented()


# Q6 -------------------------------------------------------------------------
# Define a Vehicle class with a method capacity(seats) that returns `seats`.
# Define a Bus subclass that OVERRIDES capacity() and calls super().capacity()
# but adds a standing allowance of 5 extra people. Create a Bus and return the
# overridden capacity.
#   bus_capacity(50) -> 55    (50 seated + 5 standing via super())
@quiz.question(
    "Override capacity() in Bus using super() to add 5 standing spots; return total.",
    cases=[
        ((50,), 55),
        ((0,), 5),
    ],
    answer=ANSWERS["bus_capacity"],
)
def bus_capacity(seats):
    return unimplemented()


# Q7 -------------------------------------------------------------------------
# Define a Person class with __init__(name, age) and a __str__ method that
# returns "<name> (<age>)". Create a Person and return str(person), which
# invokes __str__.
#   person_str("Alice", 30) -> "Alice (30)"
@quiz.question(
    "Define __str__ on a Person class returning '<name> (<age>)'; return str(person).",
    cases=[
        (("Alice", 30), "Alice (30)"),
        (("Bob", 0), "Bob (0)"),
    ],
    answer=ANSWERS["person_str"],
)
def person_str(name, age):
    return unimplemented()


# Q8 -------------------------------------------------------------------------
# Define a base Animal class and a Dog subclass that inherits from it. Create a
# Dog instance, then return a tuple of two isinstance checks:
#   (isinstance(dog, Dog), isinstance(dog, Animal))
# A Dog is both a Dog and an Animal, so this is always (True, True).
#   check_isinstance() -> (True, True)
@quiz.question(
    "Use isinstance to check a Dog against Dog and Animal; return (bool, bool).",
    cases=[
        ((), (True, True)),
    ],
    answer=ANSWERS["check_isinstance"],
)
def check_isinstance():
    return unimplemented()


# Q9 -------------------------------------------------------------------------
# Define a Temperature class. Add a @classmethod from_fahrenheit(f) that builds
# an instance from a Fahrenheit value (storing celsius), and a @staticmethod
# is_freezing(c) that returns True if celsius <= 0. Build an instance from the
# given Fahrenheit value and return the tuple (celsius, is_freezing).
#   temperature_tools(32) -> (0.0, True)     # 32F == 0C, which is freezing
#   temperature_tools(212) -> (100.0, False) # 212F == 100C, not freezing
@quiz.question(
    "Use a @classmethod (from_fahrenheit) and @staticmethod (is_freezing); return (celsius, freezing).",
    cases=[
        ((32,), (0.0, True)),
        ((212,), (100.0, False)),
    ],
    answer=ANSWERS["temperature_tools"],
)
def temperature_tools(fahrenheit):
    return unimplemented()


# Q10 ------------------------------------------------------------------------
# Polymorphism via method overriding. Define a base Animal class with a
# method sound() returning "...", and two subclasses Cat and Dog that OVERRIDE
# sound() to return "meow" and "woof" respectively. Given an animal kind
# ("cat" or "dog"), create the matching object and return its sound().
#   animal_sound("cat") -> "meow"
#   animal_sound("dog") -> "woof"
@quiz.question(
    "Override sound() in Cat and Dog subclasses (polymorphism); return the sound.",
    cases=[
        (("cat",), "meow"),
        (("dog",), "woof"),
    ],
    answer=ANSWERS["animal_sound"],
)
def animal_sound(kind):
    return unimplemented()


if __name__ == "__main__":
    quiz.run()
