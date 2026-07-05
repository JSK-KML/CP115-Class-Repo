import pytest
import subprocess
import sys
import os


@pytest.fixture
def exercise_path():
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'lab-4-3.py')


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


def parking_fee(hours):
    tier2 = max(0, min(hours, 5) - 2) * 2.00
    tier3 = max(0, hours - 5) * 3.00
    return min(tier2 + tier3, 30.00)


@pytest.mark.parametrize("hours", [1, 2, 3, 5, 6, 10, 4, 8, 15, 0])
def test_parking_fee(exercise_path, hours):
    context = f"input hours={hours}"
    output = run_exercise(exercise_path, f"{hours}\n")
    (result,) = read_numbers(output, 1, context)

    expected = round(parking_fee(hours), 2)
    got = round(result, 2)

    assert got == expected, f"{context} -> expected {expected} but got {got}"
