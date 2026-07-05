import pytest
import subprocess
import sys
import os


@pytest.fixture
def exercise_path():
    """Path to the student's solution file."""
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'lab-03-3.py')


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


@pytest.mark.parametrize("kilobyte", [1, 1024, 2048, 500, 1536, 1048576, 1073741824, 100.5, 5000000])
def test_storage_conversion(exercise_path, kilobyte):
    """Convert KB to MB, GB, TB, PB (divide by 1024 each step), in order."""
    context = f"input kilobyte={kilobyte}"
    output = run_exercise(exercise_path, f"{kilobyte}\n")
    megabyte, gigabyte, terabyte, petabyte = read_numbers(output, 4, context)

    checks = [
        ("megabyte", megabyte, kilobyte / 1024),
        ("gigabyte", gigabyte, kilobyte / 1024 ** 2),
        ("terabyte", terabyte, kilobyte / 1024 ** 3),
        ("petabyte", petabyte, kilobyte / 1024 ** 4),
    ]
    for name, actual, expected in checks:
        got = round(actual, 6)
        exp = round(expected, 6)
        assert got == exp, f"{context} -> {name} expected {exp} but got {got}"
