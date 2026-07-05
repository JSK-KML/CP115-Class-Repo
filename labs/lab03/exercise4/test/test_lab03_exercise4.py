import pytest
import subprocess
import sys
import os


@pytest.fixture
def exercise_path():
    """Path to the student's solution file."""
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'lab-03-4.py')


def run_exercise(exercise_path, inputs):
    """Run the solution with the given stdin and return its stdout."""
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
    """Parse exactly `count` numbers (one per line) from the output, or fail clearly."""
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


@pytest.mark.parametrize("pages", [1, 2, 3, 5, 7, 10, 20, 50, 100])
def test_fax_cost(exercise_path, pages):
    """totalCost = RM3 service charge + RM0.20 per page."""
    context = f"input pages={pages}"
    output = run_exercise(exercise_path, f"{pages}\n")
    (result,) = read_numbers(output, 1, context)

    expected = round(3 + 0.20 * pages, 2)
    got = round(result, 2)

    assert got == expected, f"{context} -> expected {expected} but got {got}"
