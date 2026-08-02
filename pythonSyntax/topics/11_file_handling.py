"""
Topic: File Handling
Source: https://pynative.com/python-file-handling-exercises/

Each exercise practices REAL file I/O. To stay deterministic, every function
receives the file CONTENT as a string, writes it to a temporary file, then
RE-OPENS and reads that file back to compute the answer. The temp file is
always cleaned up afterwards.

Fill in each function body (replace `unimplemented()`), then run:
    python topics/11_file_handling.py            # grade your solutions
    python topics/11_file_handling.py --answers  # show the answer key
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from harness import Quiz, unimplemented
from answers.a11_file_handling import ANSWERS

quiz = Quiz("File Handling")


# Q1 -------------------------------------------------------------------------
# Count the number of lines in a file.
# Given the file content as a string, write it to a temp file, read it back
# with readlines(), and return how many lines it has.
#   content="a\nb\nc" -> 3   (three lines)
#   content=""        -> 0   (empty file has no lines)
@quiz.question(
    "Count the number of lines in a file (content given as a string).",
    cases=[
        (("a\nb\nc",), 3),
        (("",), 0),
    ],
    answer=ANSWERS["count_lines"],
)
def count_lines(content):
    return unimplemented()


# Q2 -------------------------------------------------------------------------
# Count the total number of words in a file.
# Write the content to a temp file, read it back, split on whitespace, and
# return the word count.
#   content="hello world\nfoo bar" -> 4
#   content="   "                  -> 0   (only whitespace, no words)
@quiz.question(
    "Count the total number of words in a file (content given as a string).",
    cases=[
        (("hello world\nfoo bar",), 4),
        (("   ",), 0),
    ],
    answer=ANSWERS["count_words"],
)
def count_words(content):
    return unimplemented()


# Q3 -------------------------------------------------------------------------
# Count the total number of characters in a file, INCLUDING spaces and
# newline characters. Write the content out, read the whole file back as one
# string, and return its length.
#   content="a\nb" -> 3   (the two letters plus the newline)
#   content=""     -> 0
@quiz.question(
    "Count the total characters in a file, including spaces and newlines.",
    cases=[
        (("a\nb",), 3),
        (("",), 0),
    ],
    answer=ANSWERS["count_chars"],
)
def count_chars(content):
    return unimplemented()


# Q4 -------------------------------------------------------------------------
# Read only the FIRST n lines of a file.
# Write the content, read it back, and return a list of the first n lines with
# their trailing newline characters removed. If the file has fewer than n
# lines, return all of them.
#   content="a\nb\nc\nd", n=2 -> ['a', 'b']
#   content="x\ny",       n=5 -> ['x', 'y']
@quiz.question(
    "Read the first n lines of a file (newlines stripped, returned as a list).",
    cases=[
        (("a\nb\nc\nd", 2), ['a', 'b']),
        (("x\ny", 5), ['x', 'y']),
    ],
    answer=ANSWERS["read_first_n"],
)
def read_first_n(content, n):
    return unimplemented()


# Q5 -------------------------------------------------------------------------
# Read only the LAST n lines of a file.
# Write the content, read it back, and return a list of the last n lines with
# their trailing newline characters removed. If the file has fewer than n
# lines, return all of them.
#   content="a\nb\nc\nd", n=2 -> ['c', 'd']
#   content="only",       n=3 -> ['only']
@quiz.question(
    "Read the last n lines of a file (newlines stripped, returned as a list).",
    cases=[
        (("a\nb\nc\nd", 2), ['c', 'd']),
        (("only", 3), ['only']),
    ],
    answer=ANSWERS["read_last_n"],
)
def read_last_n(content, n):
    return unimplemented()


# Q6 -------------------------------------------------------------------------
# Read one specific line from a file, given a 1-based line number.
# Write the content, read the lines back, and return the requested line with
# its trailing newline stripped.
#   content="first\nsecond\nthird", lineno=2 -> 'second'
#   content="a\nb",                 lineno=1 -> 'a'
@quiz.question(
    "Return a specific line of a file by its 1-based line number (newline stripped).",
    cases=[
        (("first\nsecond\nthird", 2), 'second'),
        (("a\nb", 1), 'a'),
    ],
    answer=ANSWERS["read_specific_line"],
)
def read_specific_line(content, lineno):
    return unimplemented()


# Q7 -------------------------------------------------------------------------
# Find the LONGEST line in a file (the line with the most characters).
# Write the content, read the lines back, and return the longest line with its
# trailing newline stripped. If several lines tie, return the first one.
#   content="hi\nhello\nhey" -> 'hello'
#   content="single"         -> 'single'
@quiz.question(
    "Find the longest line in a file (newline stripped; first wins on a tie).",
    cases=[
        (("hi\nhello\nhey",), 'hello'),
        (("single",), 'single'),
    ],
    answer=ANSWERS["longest_line"],
)
def longest_line(content):
    return unimplemented()


# Q8 -------------------------------------------------------------------------
# Count how many times a specific whole word occurs in a file.
# Write the content, read it back, split into whitespace-separated words, and
# return how many equal the target word exactly.
#   content="Python is fun. Python rocks", word="Python" -> 2
#   content="no match here",               word="Python" -> 0
@quiz.question(
    "Count occurrences of a specific whole word in a file.",
    cases=[
        (("Python is fun. Python rocks", "Python"), 2),
        (("no match here", "Python"), 0),
    ],
    answer=ANSWERS["count_word_occurrences"],
)
def count_word_occurrences(content, word):
    return unimplemented()


# Q9 -------------------------------------------------------------------------
# Append a new line to a file WITHOUT overwriting it.
# Write the original content, then re-open the file in append mode ('a') and
# add `extra`. Finally re-open in read mode and return the complete contents.
#   content="line1\n", extra="line2" -> "line1\nline2"
#   content="",        extra="first" -> "first"
@quiz.question(
    "Append text to a file (append mode), then return the full contents.",
    cases=[
        (("line1\n", "line2"), "line1\nline2"),
        (("", "first"), "first"),
    ],
    answer=ANSWERS["append_line"],
)
def append_line(content, extra):
    return unimplemented()


# Q10 ------------------------------------------------------------------------
# Copy the contents of one file into a brand-new second file.
# Write the content to a source temp file, read it back, write it into a
# separate destination temp file, then read the DESTINATION and return what it
# holds (which must match the original content exactly).
#   content="hello\nworld" -> "hello\nworld"
#   content=""             -> ""
@quiz.question(
    "Copy a file's contents into a new file, then return the copy's contents.",
    cases=[
        (("hello\nworld",), "hello\nworld"),
        (("",), ""),
    ],
    answer=ANSWERS["copy_contents"],
)
def copy_contents(content):
    return unimplemented()


if __name__ == "__main__":
    quiz.run()
