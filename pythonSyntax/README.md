# Python Syntax — Topic-by-Topic Practice

A self-graded revision codebase built from the [PyNative](https://pynative.com/) exercise
collection. The scattered, duplicated online exercises are curated into **one runnable file
per topic**, each with the best questions deduplicated and rewritten as small, gradeable
functions.

## How it works

Every topic file lives in [topics/](topics/) and contains ~10 questions. Each question is:

- a **comment** describing the exercise (with a concrete example),
- a **function stub** for you to fill in (replace `return unimplemented()`),
- built-in **test cases**.

Reference solutions live in a separate [answers/](answers/) package (one module per
topic), **not** inline next to the stub — so opening a topic file to solve it doesn't
spoil the answer. Each question wires its key in via `answer=ANSWERS["func_name"]`, and
`--answers` mode pulls the reference from there. Peek only when you want to.

Run a file and it grades *your* solutions and prints `Solved X/Y correctly`.

## Usage

```bash
# Grade your solutions for one topic
python3 topics/02_dictionaries.py

# Show the answer key for a topic (also proves every question is solvable)
python3 topics/02_dictionaries.py --answers

# See the failure detail for a passing/failing question
python3 topics/02_dictionaries.py --verbose

# Grade EVERYTHING at once with a summary table
python3 run_all.py
python3 run_all.py --answers
```

## Workflow

1. Open a topic file, e.g. [topics/02_dictionaries.py](topics/02_dictionaries.py).
2. For each question, replace the `return unimplemented()` line with your solution.
3. Run the file. Iterate until you hit `Solved 10/10`.
4. Stuck? Run with `--answers` to reveal the reference solution.

## Topics

| File | Topic |
|------|-------|
| [01_data_structures.py](topics/01_data_structures.py) | Lists, tuples, strings, basic dict/set ops |
| [02_dictionaries.py](topics/02_dictionaries.py) | Dictionaries |
| [03_sets.py](topics/03_sets.py) | Sets |
| [04_input_output.py](topics/04_input_output.py) | Input / output & string formatting |
| [05_comprehensions.py](topics/05_comprehensions.py) | List/dict/set comprehensions |
| [06_collections_module.py](topics/06_collections_module.py) | `collections` (Counter, deque, …) |
| [07_datetime.py](topics/07_datetime.py) | Date & time |
| [08_oop.py](topics/08_oop.py) | Object-oriented programming |
| [09_math_statistics.py](topics/09_math_statistics.py) | `math` & `statistics` |
| [10_os_sys.py](topics/10_os_sys.py) | `os` & `sys` |
| [11_file_handling.py](topics/11_file_handling.py) | File handling |
| [12_exception_handling.py](topics/12_exception_handling.py) | Exceptions |
| [13_iterators_generators.py](topics/13_iterators_generators.py) | Iterators & generators |
| [14_itertools_functools.py](topics/14_itertools_functools.py) | `itertools` & `functools` |
| [15_random.py](topics/15_random.py) | Random numbers |
| [16_intermediate.py](topics/16_intermediate.py) | Intermediate (functions, recursion, decorators) |

## Notes on design

- Every exercise is a **pure, deterministic function** so it can be auto-graded — questions
  that were originally about `print`/`input`, real files, the clock, or randomness have been
  reframed (e.g. file exercises write to a temp file internally; random exercises take a
  `seed`; datetime exercises take explicit dates).
- No third-party dependencies — standard library only. Requires Python 3.8+.
