"""
Topic: os and sys Modules
Source: https://pynative.com/python-os-sys-module-exercises/

Fill in each function body (replace `unimplemented()`), then run:
    python topics/10_os_sys.py            # grade your solutions
    python topics/10_os_sys.py --answers  # show the answer key

Note: several exercises in the source touch the real filesystem/environment,
which is not deterministically gradeable. They have been reframed here so every
answer is fully reproducible:
  - os.path.* questions operate on given path STRINGS (pure functions).
  - Genuine filesystem operations build their own scratch area with `tempfile`
    inside the function, act on it, return a deterministic result, and clean up.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from harness import Quiz, unimplemented
from answers.a10_os_sys import ANSWERS

import tempfile
import shutil

quiz = Quiz("os and sys Modules")


# Q1 -------------------------------------------------------------------------
# Split a filename into its root and extension using os.path.splitext.
# The extension keeps its leading dot; a name with no extension gives ''.
#   'file.txt'  -> ('file', '.txt')
#   'README'    -> ('README', '')
@quiz.question(
    "Split a filename into (root, extension) with os.path.splitext.",
    cases=[
        (("file.txt",), ("file", ".txt")),
        (("archive.tar.gz",), ("archive.tar", ".gz")),
        (("README",), ("README", "")),
    ],
    answer=ANSWERS["split_extension"],
)
def split_extension(name):
    return unimplemented()


# Q2 -------------------------------------------------------------------------
# Return the final component (the file name) of a path using os.path.basename.
#   '/home/user/file.txt' -> 'file.txt'
#   'noslash.txt'         -> 'noslash.txt'
@quiz.question(
    "Return the last component of a path string with os.path.basename.",
    cases=[
        (("/home/user/file.txt",), "file.txt"),
        (("noslash.txt",), "noslash.txt"),
    ],
    answer=ANSWERS["base_name"],
)
def base_name(path):
    return unimplemented()


# Q3 -------------------------------------------------------------------------
# Return the directory portion of a path using os.path.dirname.
#   '/home/user/file.txt' -> '/home/user'
#   'file.txt'            -> ''   (no directory part)
@quiz.question(
    "Return the directory portion of a path string with os.path.dirname.",
    cases=[
        (("/home/user/file.txt",), "/home/user"),
        (("file.txt",), ""),
    ],
    answer=ANSWERS["dir_name"],
)
def dir_name(path):
    return unimplemented()


# Q4 -------------------------------------------------------------------------
# Join a list of path components into one path with os.path.join.
# On macOS/Linux the separator is '/'.
#   ['home', 'user', 'file.txt'] -> 'home/user/file.txt'
#   ['a', 'b', 'c']              -> 'a/b/c'
@quiz.question(
    "Join a list of components into a single path with os.path.join.",
    cases=[
        ((["home", "user", "file.txt"],), "home/user/file.txt"),
        ((["a", "b", "c"],), "a/b/c"),
    ],
    answer=ANSWERS["join_path"],
)
def join_path(parts):
    return unimplemented()


# Q5 -------------------------------------------------------------------------
# Split a path into a (head, tail) pair with os.path.split, where tail is the
# last component and head is everything before it.
#   '/home/user/file.txt' -> ('/home/user', 'file.txt')
#   'file.txt'            -> ('', 'file.txt')
@quiz.question(
    "Split a path into (head, tail) with os.path.split.",
    cases=[
        (("/home/user/file.txt",), ("/home/user", "file.txt")),
        (("file.txt",), ("", "file.txt")),
    ],
    answer=ANSWERS["split_path"],
)
def split_path(path):
    return unimplemented()


# Q6 -------------------------------------------------------------------------
# Report whether a path is absolute using os.path.isabs.
# On macOS/Linux an absolute path starts with '/'.
#   '/home/user' -> True
#   'home/user'  -> False
@quiz.question(
    "Return True if the path is absolute (os.path.isabs).",
    cases=[
        (("/home/user",), True),
        (("home/user",), False),
    ],
    answer=ANSWERS["is_absolute"],
)
def is_absolute(path):
    return unimplemented()


# Q7 -------------------------------------------------------------------------
# Read command-line arguments. sys.argv[0] is always the script name, so the
# real arguments are everything after it. Given a list that models sys.argv,
# return just the user arguments (argv[1:]).
#   ['prog.py', 'x', 'y'] -> ['x', 'y']
#   ['prog.py']           -> []
@quiz.question(
    "Return the user arguments from a sys.argv-style list (drop argv[0]).",
    cases=[
        ((["prog.py", "x", "y"],), ["x", "y"]),
        ((["prog.py"],), []),
    ],
    answer=ANSWERS["script_args"],
)
def script_args(argv):
    return unimplemented()


# Q8 -------------------------------------------------------------------------
# Create a directory (with tempfile), add three files to it, then return the
# sorted list of file names inside it. Cleans up the directory afterwards.
# Takes no external path; builds and removes its own scratch dir.
#   () -> ['a.txt', 'b.txt', 'c.txt']
@quiz.question(
    "Create a temp dir, add 3 files, return the sorted list of their names.",
    cases=[
        ((), ["a.txt", "b.txt", "c.txt"]),
    ],
    answer=ANSWERS["list_created_files"],
)
def list_created_files():
    return unimplemented()


# Q9 -------------------------------------------------------------------------
# Calculate the total size (in bytes) of every file in a directory tree.
# Builds a temp dir with files whose contents are 3, 2 and 1 ASCII bytes,
# sums each file's size with os.path.getsize, then cleans up.
#   () -> 6   (3 + 2 + 1 bytes)
@quiz.question(
    "Build a temp dir of files (3+2+1 bytes) and return the total size in bytes.",
    cases=[
        ((), 6),
    ],
    answer=ANSWERS["directory_size"],
)
def directory_size():
    return unimplemented()


# Q10 ------------------------------------------------------------------------
# Recursively find files by extension. Builds a temp tree with 'a.txt',
# 'b.log' and 'sub/c.txt', walks it with os.walk, keeps only the '.txt' files
# (matched via os.path.splitext), and returns their sorted paths relative to
# the tree root. Cleans up afterwards.
#   () -> ['a.txt', 'sub/c.txt']
@quiz.question(
    "Walk a temp tree and return the sorted relative paths of all '.txt' files.",
    cases=[
        ((), ["a.txt", "sub/c.txt"]),
    ],
    answer=ANSWERS["find_txt_files"],
)
def find_txt_files():
    return unimplemented()


if __name__ == "__main__":
    quiz.run()
