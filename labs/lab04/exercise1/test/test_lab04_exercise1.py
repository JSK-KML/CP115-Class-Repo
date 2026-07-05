import pytest
import subprocess
import sys
import os


@pytest.fixture
def exercise_path():
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'lab-4-1.py')


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


def electricity_bill(kwh):
    tier1 = min(kwh, 100) * 0.30
    tier2 = max(0, min(kwh, 200) - 100) * 0.50
    tier3 = max(0, kwh - 200) * 0.75
    return tier1 + tier2 + tier3


@pytest.mark.parametrize("kwh", [50, 100, 150, 200, 250, 0, 101, 300, 175, 500])
def test_electricity_bill(exercise_path, kwh):
    context = f"input kwh={kwh}"
    output = run_exercise(exercise_path, f"{kwh}\n")
    (result,) = read_numbers(output, 1, context)

    expected = round(electricity_bill(kwh), 2)
    got = round(result, 2)

    assert got == expected, f"{context} -> expected {expected} but got {got}"
