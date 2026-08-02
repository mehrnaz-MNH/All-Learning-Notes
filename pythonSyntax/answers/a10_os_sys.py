"""Reference answers for 10_os_sys.py.

Kept out of the topic file so solving a question doesn't spoil it.
Shown only by `--answers` mode via ANSWERS[func_name]."""

import os, sys
import tempfile
import shutil


def _make_files_and_list():
    d = tempfile.mkdtemp()
    try:
        for name in ["b.txt", "a.txt", "c.txt"]:
            with open(os.path.join(d, name), "w") as f:
                f.write("x")
        return sorted(os.listdir(d))
    finally:
        shutil.rmtree(d)


def _total_dir_size():
    d = tempfile.mkdtemp()
    try:
        for i, content in enumerate(["aaa", "bb", "c"]):
            with open(os.path.join(d, "f%d.dat" % i), "w") as f:
                f.write(content)
        total = 0
        for name in os.listdir(d):
            total += os.path.getsize(os.path.join(d, name))
        return total
    finally:
        shutil.rmtree(d)


def _find_txt_files():
    root = tempfile.mkdtemp()
    try:
        os.makedirs(os.path.join(root, "sub"))
        for rel in ["a.txt", "b.log", os.path.join("sub", "c.txt")]:
            with open(os.path.join(root, rel), "w") as f:
                f.write("x")
        matches = []
        for dirpath, _dirnames, filenames in os.walk(root):
            for fn in filenames:
                if os.path.splitext(fn)[1] == ".txt":
                    full = os.path.join(dirpath, fn)
                    matches.append(os.path.relpath(full, root))
        return sorted(matches)
    finally:
        shutil.rmtree(root)


ANSWERS = {
    "split_extension": lambda name: os.path.splitext(name),
    "base_name": lambda path: os.path.basename(path),
    "dir_name": lambda path: os.path.dirname(path),
    "join_path": lambda parts: os.path.join(*parts),
    "split_path": lambda path: os.path.split(path),
    "is_absolute": lambda path: os.path.isabs(path),
    "script_args": lambda argv: argv[1:],
    "list_created_files": lambda: _make_files_and_list(),
    "directory_size": lambda: _total_dir_size(),
    "find_txt_files": lambda: _find_txt_files(),
}
