import pytest
import subprocess
import sys
import os


@pytest.fixture
def exercise_path():
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'lab-4-5.py')


def run_exercise(exercise_path, inputs):
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


def read_numbers(output, count, context):
    lines = output.strip().split('\n') if output.strip() else []
    if len(lines) != count:
        pytest.fail(
            f"{context}: expected {count} line(s) of output but got {len(lines)}. "
            f"Actual output: {output!r}"
        )
    try:
        return [float(line) for line in lines]
    except ValueError:
        pytest.fail(
            f"{context}: every output line must be a plain number. "
            f"Actual output: {output!r}"
        )


def football_points(scoreA, scoreB):
    if scoreA > scoreB:
        pointsA = 3
    elif scoreA == scoreB:
        pointsA = 1
    else:
        pointsA = 0

    if scoreB > scoreA:
        pointsB = 3
    elif scoreB == scoreA:
        pointsB = 1
    else:
        pointsB = 0

    if scoreB == 0:
        pointsA += 1
    if scoreA == 0:
        pointsB += 1

    return pointsA, pointsB


@pytest.mark.parametrize("scoreA,scoreB", [
    (2, 1),
    (1, 2),
    (0, 0),
    (3, 0),
    (0, 3),
    (1, 1),
    (2, 0),
    (0, 2),
    (2, 2),
    (5, 4),
])
def test_football_points(exercise_path, scoreA, scoreB):
    context = f"inputs scoreA={scoreA}, scoreB={scoreB}"
    inputs = f"{scoreA}\n{scoreB}\n"
    output = run_exercise(exercise_path, inputs)
    resultA, resultB = read_numbers(output, 2, context)

    expectedA, expectedB = football_points(scoreA, scoreB)
    gotA, gotB = round(resultA, 2), round(resultB, 2)

    assert (gotA, gotB) == (expectedA, expectedB), (
        f"{context} -> expected pointsA={expectedA}, pointsB={expectedB} "
        f"but got pointsA={gotA}, pointsB={gotB}"
    )
