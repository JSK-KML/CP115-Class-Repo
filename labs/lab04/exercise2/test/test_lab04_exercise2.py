import pytest
import subprocess
import sys
import os


@pytest.fixture
def exercise_path():
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'lab-4-2.py')


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


def income_tax(income):
    tier2 = max(0, min(income, 100000) - 50000) * 0.01
    tier3 = max(0, income - 100000) * 0.02
    return tier2 + tier3


@pytest.mark.parametrize("income", [
    30000, 50000, 75000, 100000, 150000,
    0, 60000, 200000, 99000, 120000,
])
def test_income_tax(exercise_path, income):
    context = f"input income={income}"
    output = run_exercise(exercise_path, f"{income}\n")
    (result,) = read_numbers(output, 1, context)

    expected = round(income_tax(income), 2)
    got = round(result, 2)

    assert got == expected, f"{context} -> expected {expected} but got {got}"
