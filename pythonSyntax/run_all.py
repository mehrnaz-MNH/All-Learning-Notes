"""
Grade every topic at once.

    python run_all.py            # grade YOUR solutions across all topics
    python run_all.py --answers  # run the answer key (verifies all topics work)

Each topic file is imported and its module-level `quiz` object is run.
"""
import os
import sys
import importlib.util

TOPICS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "topics")


def load_quiz(path):
    spec = importlib.util.spec_from_file_location(
        os.path.splitext(os.path.basename(path))[0], path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, "quiz", None)


def main():
    argv = sys.argv[1:]
    files = sorted(f for f in os.listdir(TOPICS_DIR)
                   if f.endswith(".py") and not f.startswith("_"))

    total_solved = total_questions = 0
    per_topic = []

    for f in files:
        quiz = load_quiz(os.path.join(TOPICS_DIR, f))
        if quiz is None:
            continue
        solved, total = quiz.run(argv)
        total_solved += solved
        total_questions += total
        per_topic.append((quiz.title, solved, total))

    print("=" * 44)
    print(" OVERALL SUMMARY")
    print("=" * 44)
    for title, solved, total in per_topic:
        bar = "#" * solved + "-" * (total - solved)
        print(f"  {title:<26} {solved:>2}/{total:<2}  {bar}")
    print("-" * 44)
    print(f"  {'TOTAL':<26} {total_solved:>2}/{total_questions}")
    print("=" * 44)


if __name__ == "__main__":
    main()
