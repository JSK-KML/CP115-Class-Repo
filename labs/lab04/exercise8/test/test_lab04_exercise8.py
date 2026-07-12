import pytest
import subprocess
import sys
import os


@pytest.fixture
def exercise_path():
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'lab-4-8.py')


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


def taxi_fare(distance, afterMidnight):
    fare = 4.0 + max(0, distance - 2) * 1.20
    if afterMidnight == "yes":
        fare += 3.0
    return fare


@pytest.mark.parametrize("distance,afterMidnight", [
    (0, "no"),
    (2, "no"),
    (5, "no"),
    (5, "yes"),
    (10, "no"),
    (10, "yes"),
    (1, "yes"),
    (3, "no"),
    (20, "no"),
    (0, "yes"),
])
def test_taxi_fare(exercise_path, distance, afterMidnight):
    context = f"inputs distance={distance}, afterMidnight={afterMidnight}"
    inputs = f"{distance}\n{afterMidnight}\n"
    output = run_exercise(exercise_path, inputs)
    (result,) = read_numbers(output, 1, context)

    expected = round(taxi_fare(distance, afterMidnight), 2)
    got = round(result, 2)

    assert got == expected, f"{context} -> expected {expected} but got {got}"
