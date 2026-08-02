"""
Tiny test harness for the Python practice codebase.

Every topic file registers questions against a Quiz object. Each question has:
  - a description  (the exercise prompt, shown when it fails)
  - cases          (list of (args_tuple, expected) pairs used to check correctness)
  - answer         (a reference solution, used by --answers mode / self-check)
  - your solution  (the decorated function body you fill in)

Run a topic file to grade YOUR solutions:
    python topics/02_dictionaries.py

Run with the answer key (also verifies every question is solvable):
    python topics/02_dictionaries.py --answers

Grade everything at once:
    python run_all.py
    python run_all.py --answers
"""

import sys
import io
import contextlib


class Quiz:
    def __init__(self, title):
        self.title = title
        self.questions = []

    def question(self, description, cases, answer, compare=None):
        """Decorator. Register a question.

        description : str            -> the exercise prompt
        cases       : list[(args, expected)]  -> args is a tuple passed as *args
        answer      : callable       -> reference solution (the answer key)
        compare     : callable(got, expected) -> bool, optional custom comparison
        """
        def decorator(func):
            self.questions.append({
                "description": description,
                "cases": cases,
                "answer": answer,
                "user": func,
                "compare": compare or (lambda got, exp: got == exp),
            })
            return func
        return decorator

    def _run_one(self, q, use_answer):
        fn = q["answer"] if use_answer else q["user"]
        for args, expected in q["cases"]:
            try:
                got = fn(*args)
            except NotImplementedError:
                return (False, f"not attempted (args={args!r})")
            except Exception as exc:
                return (False, f"raised {type(exc).__name__}: {exc} (args={args!r})")
            if not q["compare"](got, expected):
                return (False, f"args={args!r} -> got {got!r}, expected {expected!r}")
        return (True, "")

    def run(self, argv=None):
        argv = sys.argv[1:] if argv is None else argv
        use_answer = "--answers" in argv or "-a" in argv
        verbose = "--verbose" in argv or "-v" in argv

        mode = "ANSWER KEY" if use_answer else "YOUR SOLUTIONS"
        print(f"\n=== {self.title}  ({mode}) ===")

        solved = 0
        for i, q in enumerate(self.questions, 1):
            ok, detail = self._run_one(q, use_answer)
            if ok:
                solved += 1
                print(f"  [PASS] Q{i}")
            else:
                print(f"  [FAIL] Q{i}: {q['description'].strip().splitlines()[0]}")
                if verbose or not use_answer:
                    print(f"         -> {detail}")

        total = len(self.questions)
        print(f"  ----")
        print(f"  Solved {solved}/{total} correctly.\n")
        return solved, total


def unimplemented():
    """Marker for an unattempted solution stub."""
    raise NotImplementedError
