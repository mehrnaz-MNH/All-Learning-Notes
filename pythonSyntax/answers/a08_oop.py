"""Reference answers for 08_oop.py.

Kept out of the topic file so solving a question doesn't spoil it.
Shown only by `--answers` mode via ANSWERS[func_name]."""

import os, sys


def _q1_answer(name, max_speed):
    class Vehicle:
        def __init__(self, name, max_speed):
            self.name = name
            self.max_speed = max_speed

        def describe(self):
            return f"{self.name} goes {self.max_speed}"
    return Vehicle(name, max_speed).describe()


def _q2_answer(n):
    class Counter:
        count = 0

        def __init__(self):
            Counter.count += 1
    for _ in range(n):
        Counter()
    return Counter.count


def _q3_answer(width, height):
    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height

        def perimeter(self):
            return 2 * (self.width + self.height)
    r = Rectangle(width, height)
    return (r.area(), r.perimeter())


def _q4_answer(balance, amount):
    class BankAccount:
        def __init__(self, balance):
            self.balance = balance

        def withdraw(self, amount):
            if amount <= self.balance:
                self.balance -= amount
    acct = BankAccount(balance)
    acct.withdraw(amount)
    return acct.balance


def _q5_answer(name, max_speed):
    class Vehicle:
        def __init__(self, name, max_speed):
            self.name = name
            self.max_speed = max_speed

    class Bus(Vehicle):
        pass
    b = Bus(name, max_speed)
    return f"{b.name} - {b.max_speed}"


def _q6_answer(seats):
    class Vehicle:
        def capacity(self, seats):
            return seats

    class Bus(Vehicle):
        def capacity(self, seats):
            return super().capacity(seats) + 5
    return Bus().capacity(seats)


def _q7_answer(name, age):
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __str__(self):
            return f"{self.name} ({self.age})"
    return str(Person(name, age))


def _q8_answer():
    class Animal:
        pass

    class Dog(Animal):
        pass
    dog = Dog()
    return (isinstance(dog, Dog), isinstance(dog, Animal))


def _q9_answer(fahrenheit):
    class Temperature:
        def __init__(self, celsius):
            self.celsius = celsius

        @classmethod
        def from_fahrenheit(cls, f):
            return cls((f - 32) * 5 / 9)

        @staticmethod
        def is_freezing(c):
            return c <= 0
    t = Temperature.from_fahrenheit(fahrenheit)
    return (t.celsius, Temperature.is_freezing(t.celsius))


def _q10_answer(kind):
    class Animal:
        def sound(self):
            return "..."

    class Cat(Animal):
        def sound(self):
            return "meow"

    class Dog(Animal):
        def sound(self):
            return "woof"
    animal = Cat() if kind == "cat" else Dog()
    return animal.sound()


ANSWERS = {
    "vehicle_describe": _q1_answer,
    "count_instances": _q2_answer,
    "rectangle_stats": _q3_answer,
    "withdraw_protected": _q4_answer,
    "bus_info": _q5_answer,
    "bus_capacity": _q6_answer,
    "person_str": _q7_answer,
    "check_isinstance": _q8_answer,
    "temperature_tools": _q9_answer,
    "animal_sound": _q10_answer,
}
