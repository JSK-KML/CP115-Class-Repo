import pytest
import subprocess
import sys
import os


@pytest.fixture
def exercise_path():
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'exercise6.py')


def run_exercise(exercise_path, inputs):
    if not os.path.isfile(exercise_path):
        pytest.fail("exercise6.py was not found in the exercise6 folder")

    process = subprocess.Popen(
        [sys.executable, exercise_path],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    try:
        stdout, stderr = process.communicate(input=inputs, timeout=30)
    except subprocess.TimeoutExpired:
        process.kill()
        process.communicate()
        pytest.fail("the program took too long to finish (over 30 seconds) - check for an infinite loop")

    if process.returncode != 0:
        error = stderr.strip().splitlines()[-1] if stderr.strip() else "the program crashed"
        pytest.fail(f"the program did not run: {error}")

    return stdout


def read_lines(output, count, context):
    lines = output.replace("\r\n", "\n").strip().split('\n') if output.strip() else []
    if len(lines) != count:
        pytest.fail(
            f"{context}: expected {count} line(s) of output but got {len(lines)}. "
            f"Actual output: {output!r}"
        )
    return lines


def overtaken(rounds):
    # rounds is a list of (a, b) pairs. Return the first round number (1-based)
    # where b > a, or 0 if it never happens.
    round_number = 0
    for a, b in rounds:
        round_number += 1
        if b > a:
            return round_number
    return 0


CASES = [
    [(100, 90), (150, 140), (200, 210)],
    [(50, 60)],
    [(100, 90), (200, 190)],
    [(10, 20), (30, 40)],
    [(100, 100), (100, 101)],
    [(5, 4), (6, 5), (7, 6), (8, 9)],
    [(300, 100), (400, 350), (500, 450)],
    [(1, 2)],
    [(80, 70), (90, 80), (100, 110)],
    [(60, 60), (70, 70), (80, 80)],
]


@pytest.mark.parametrize("rounds", CASES)
def test_overtaken(exercise_path, rounds):
    context = f"input rounds={rounds}"
    # Flatten pairs into A, B, A, B, ... then end with -1.
    nums = []
    for a, b in rounds:
        nums.append(a)
        nums.append(b)
    inputs = "".join(f"{n}\n" for n in nums) + "-1\n"
    output = run_exercise(exercise_path, inputs)
    (line1,) = read_lines(output, 1, context)

    expected = overtaken(rounds)

    assert line1 == str(expected), f"{context} -> overtake round expected {expected} but got {line1!r}"
