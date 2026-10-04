import pytest
import subprocess
import sys
import os


@pytest.fixture
def exercise_path():
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'exercise5.py')


def run_exercise(exercise_path, inputs):
    if not os.path.isfile(exercise_path):
        pytest.fail("exercise5.py was not found in the exercise5 folder")

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


def lucky_dip(numbers):
    score = 0
    ignored = 0
    for n in numbers:
        if n > score:
            score += n
        else:
            ignored += 1
    return score, ignored


CASES = [
    [5, 3, 8, 8, 20],
    [10, 20, 30],
    [30, 20, 10],
    [5, 5, 5],
    [1, 2, 3, 4, 5],
    [100],
    [50, 40, 60, 10, 70],
    [7, 7, 8, 8, 9],
    [2, 1, 4, 3, 6],
    [10, 10, 10, 10],
]


@pytest.mark.parametrize("numbers", CASES)
def test_lucky_dip(exercise_path, numbers):
    context = f"input numbers={numbers}"
    inputs = "".join(f"{n}\n" for n in numbers) + "0\n"
    output = run_exercise(exercise_path, inputs)
    line1, line2 = read_lines(output, 2, context)

    exp_score, exp_ignored = lucky_dip(numbers)

    assert line1 == str(exp_score), f"{context} -> final score expected {exp_score} but got {line1!r}"
    assert line2 == str(exp_ignored), f"{context} -> ignored count expected {exp_ignored} but got {line2!r}"
