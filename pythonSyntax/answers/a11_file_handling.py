"""Reference answers for 11_file_handling.py.

Kept out of the topic file so solving a question doesn't spoil it.
Shown only by `--answers` mode via ANSWERS[func_name]."""

import os, sys


def _q1_answer(content):
    import tempfile, os
    fd, path = tempfile.mkstemp(text=True)
    try:
        with open(path, 'w') as f:
            f.write(content)
        with open(path) as f:
            return len(f.readlines())
    finally:
        os.close(fd)
        os.remove(path)


def _q2_answer(content):
    import tempfile, os
    fd, path = tempfile.mkstemp(text=True)
    try:
        with open(path, 'w') as f:
            f.write(content)
        with open(path) as f:
            return len(f.read().split())
    finally:
        os.close(fd)
        os.remove(path)


def _q3_answer(content):
    import tempfile, os
    fd, path = tempfile.mkstemp(text=True)
    try:
        with open(path, 'w') as f:
            f.write(content)
        with open(path) as f:
            return len(f.read())
    finally:
        os.close(fd)
        os.remove(path)


def _q4_answer(content, n):
    import tempfile, os
    fd, path = tempfile.mkstemp(text=True)
    try:
        with open(path, 'w') as f:
            f.write(content)
        with open(path) as f:
            lines = f.readlines()
        return [line.rstrip('\n') for line in lines[:n]]
    finally:
        os.close(fd)
        os.remove(path)


def _q5_answer(content, n):
    import tempfile, os
    fd, path = tempfile.mkstemp(text=True)
    try:
        with open(path, 'w') as f:
            f.write(content)
        with open(path) as f:
            lines = f.readlines()
        return [line.rstrip('\n') for line in lines[-n:]] if n > 0 else []
    finally:
        os.close(fd)
        os.remove(path)


def _q6_answer(content, lineno):
    import tempfile, os
    fd, path = tempfile.mkstemp(text=True)
    try:
        with open(path, 'w') as f:
            f.write(content)
        with open(path) as f:
            lines = f.readlines()
        return lines[lineno - 1].rstrip('\n')
    finally:
        os.close(fd)
        os.remove(path)


def _q7_answer(content):
    import tempfile, os
    fd, path = tempfile.mkstemp(text=True)
    try:
        with open(path, 'w') as f:
            f.write(content)
        with open(path) as f:
            lines = [line.rstrip('\n') for line in f.readlines()]
        return max(lines, key=len)
    finally:
        os.close(fd)
        os.remove(path)


def _q8_answer(content, word):
    import tempfile, os
    fd, path = tempfile.mkstemp(text=True)
    try:
        with open(path, 'w') as f:
            f.write(content)
        with open(path) as f:
            return f.read().split().count(word)
    finally:
        os.close(fd)
        os.remove(path)


def _q9_answer(content, extra):
    import tempfile, os
    fd, path = tempfile.mkstemp(text=True)
    try:
        with open(path, 'w') as f:
            f.write(content)
        with open(path, 'a') as f:
            f.write(extra)
        with open(path) as f:
            return f.read()
    finally:
        os.close(fd)
        os.remove(path)


def _q10_answer(content):
    import tempfile, os
    fd_src, src = tempfile.mkstemp(text=True)
    fd_dst, dst = tempfile.mkstemp(text=True)
    try:
        with open(src, 'w') as f:
            f.write(content)
        with open(src) as f:
            data = f.read()
        with open(dst, 'w') as f:
            f.write(data)
        with open(dst) as f:
            return f.read()
    finally:
        os.close(fd_src)
        os.close(fd_dst)
        os.remove(src)
        os.remove(dst)


ANSWERS = {
    "count_lines": _q1_answer,
    "count_words": _q2_answer,
    "count_chars": _q3_answer,
    "read_first_n": _q4_answer,
    "read_last_n": _q5_answer,
    "read_specific_line": _q6_answer,
    "longest_line": _q7_answer,
    "count_word_occurrences": _q8_answer,
    "append_line": _q9_answer,
    "copy_contents": _q10_answer,
}
