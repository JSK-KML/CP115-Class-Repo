import pytest
import subprocess
import sys
import os


@pytest.fixture
def exercise_path():
    """Path to the student's solution file."""
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'lab-03-7.py')


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


@pytest.mark.parametrize("celsius", [0, 100, 37, -40, 25, -273.15, 50, -10, 98.6, 15.5])
def test_temperature_conversion(exercise_path, celsius):
    """Convert Celsius to Fahrenheit then Kelvin, in order."""
    context = f"input celsius={celsius}"
    output = run_exercise(exercise_path, f"{celsius}\n")
    fahrenheit, kelvin = read_numbers(output, 2, context)

    checks = [
        ("fahrenheit", fahrenheit, celsius * 9 / 5 + 32),
        ("kelvin", kelvin, celsius + 273.15),
    ]
    for name, actual, expected in checks:
        got = round(actual, 2)
        exp = round(expected, 2)
        assert got == exp, f"{context} -> {name} expected {exp} but got {got}"
