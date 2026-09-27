import pytest
import subprocess
import sys
import os


@pytest.fixture
def exercise_path():
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'exercise1.py')


def run_exercise(exercise_path, inputs):
    if not os.path.isfile(exercise_path):
        pytest.fail("exercise1.py was not found in the exercise1 folder")

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


def calm_streak(speeds):
    total = 0
    current = 0
    longest = 0
    for s in speeds:
        total += 1
        if s < 20:
            current += 1
        else:
            current = 0
        if current > longest:
            longest = current
    return total, longest


CASES = [
    [15, 10, 25, 8, 12, 5, 30],
    [5, 4, 3, 2, 1],
    [30, 40, 50],
    [10, 20, 10, 20, 10],
    [19, 19, 20, 19],
    [25],
    [5],
    [21, 22, 5, 6, 7, 8, 30],
    [10, 10, 10, 50, 10, 10],
    [20, 20, 20],
]


@pytest.mark.parametrize("speeds", CASES)
def test_calm_streak(exercise_path, speeds):
    context = f"input speeds={speeds}"
    inputs = "".join(f"{s}\n" for s in speeds) + "-1\n"
    output = run_exercise(exercise_path, inputs)
    line1, line2 = read_lines(output, 2, context)

    exp_total, exp_longest = calm_streak(speeds)

    assert line1 == str(exp_total), f"{context} -> total readings expected {exp_total} but got {line1!r}"
    assert line2 == str(exp_longest), f"{context} -> longest calm streak expected {exp_longest} but got {line2!r}"
