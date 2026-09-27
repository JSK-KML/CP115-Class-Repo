import pytest
import subprocess
import sys
import os


@pytest.fixture
def exercise_path():
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'exercise2.py')


def run_exercise(exercise_path, inputs):
    if not os.path.isfile(exercise_path):
        pytest.fail("exercise2.py was not found in the exercise2 folder")

    process = subprocess.Popen(
        [sys.executable, exercise_path],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    stdout, stderr = process.communicate(input=inputs)

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


def winning_margin(scores):
    total_a = 0
    total_b = 0
    turn = 1
    for s in scores:
        if turn % 2 == 1:
            total_a += s
        else:
            total_b += s
        turn += 1
    if total_a > total_b:
        winner = "A"
    elif total_b > total_a:
        winner = "B"
    else:
        winner = "Tie"
    return total_a, total_b, winner


CASES = [
    [10, 8, 5, 12, 7],
    [10, 10],
    [5, 3, 5, 3],
    [20],
    [1, 2, 3, 4, 5, 6],
    [50, 10, 10, 10],
    [7, 7, 7],
    [100, 40, 30, 30],
    [2, 9],
    [15, 15, 15, 15, 15],
]


@pytest.mark.parametrize("scores", CASES)
def test_winning_margin(exercise_path, scores):
    context = f"input scores={scores}"
    inputs = "".join(f"{s}\n" for s in scores) + "-1\n"
    output = run_exercise(exercise_path, inputs)
    line1, line2, line3 = read_lines(output, 3, context)

    exp_a, exp_b, exp_winner = winning_margin(scores)

    assert line1 == str(exp_a), f"{context} -> Player A total expected {exp_a} but got {line1!r}"
    assert line2 == str(exp_b), f"{context} -> Player B total expected {exp_b} but got {line2!r}"
    assert line3 == exp_winner, f"{context} -> winner expected {exp_winner!r} but got {line3!r}"
