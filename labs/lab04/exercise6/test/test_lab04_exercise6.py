import pytest
import subprocess
import sys
import os


@pytest.fixture
def exercise_path():
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'lab-4-6.py')


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


def concert_price(minutesBefore, membership):
    if minutesBefore < 0:
        return 0.0
    price = 80.0
    if minutesBefore > 30:
        price -= 15.0
    if membership == "yes":
        price *= 0.85
    return price


@pytest.mark.parametrize("minutesBefore,membership", [
    (60, "no"),
    (60, "yes"),
    (30, "no"),
    (30, "yes"),
    (20, "no"),
    (20, "yes"),
    (0, "no"),
    (-5, "no"),
    (-10, "yes"),
    (45, "yes"),
])
def test_concert_price(exercise_path, minutesBefore, membership):
    context = f"inputs minutesBefore={minutesBefore}, membership={membership}"
    inputs = f"{minutesBefore}\n{membership}\n"
    output = run_exercise(exercise_path, inputs)
    (result,) = read_numbers(output, 1, context)

    expected = round(concert_price(minutesBefore, membership), 2)
    got = round(result, 2)

    assert got == expected, f"{context} -> expected {expected} but got {got}"
