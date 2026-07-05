import pytest
import subprocess
import sys
import os


@pytest.fixture
def exercise_path():
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'lab-4-4.py')


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


def final_price(weight, ticketPrice):
    if weight == 0:
        return ticketPrice - 10.00
    excess = max(0, weight - 15)
    return ticketPrice + excess * 4.00


@pytest.mark.parametrize("weight,ticketPrice", [
    (0, 500),
    (10, 500),
    (15, 500),
    (20, 500),
    (25, 800),
    (5, 300),
    (30, 1000),
    (16, 450),
    (0, 1200),
    (12, 750),
])
def test_baggage_final_price(exercise_path, weight, ticketPrice):
    context = f"inputs weight={weight}, ticketPrice={ticketPrice}"
    inputs = f"{weight}\n{ticketPrice}\n"
    output = run_exercise(exercise_path, inputs)
    (result,) = read_numbers(output, 1, context)

    expected = round(final_price(weight, ticketPrice), 2)
    got = round(result, 2)

    assert got == expected, f"{context} -> expected {expected} but got {got}"
