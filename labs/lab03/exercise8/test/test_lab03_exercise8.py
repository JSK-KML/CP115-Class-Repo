import pytest
import subprocess
import sys
import os


@pytest.fixture
def exercise_path():
    """Path to the student's solution file."""
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'lab-03-8.py')


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

    if stderr:
        pytest.fail(f"Error running script: {stderr}")

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


@pytest.mark.parametrize("principal,rate,time", [
    (1000, 5, 1),
    (2000, 3.5, 2),
    (5000, 10, 3),
    (1500, 4, 1.5),
    (10000, 2, 5),
    (800, 6, 2),
    (2500, 8, 4),
    (1200, 5, 1),
    (3000, 7, 3),
    (500, 12, 0.5),
])
def test_simple_interest(exercise_path, principal, rate, time):
    """interest = P*R*T/100; total = P + interest; monthly = interest/(T*12). In order."""
    context = f"inputs principal={principal}, rate={rate}, time={time}"
    inputs = f"{principal}\n{rate}\n{time}\n"
    output = run_exercise(exercise_path, inputs)
    interest, totalAmount, monthlyInterest = read_numbers(output, 3, context)

    expected_interest = principal * rate * time / 100
    checks = [
        ("interest", interest, expected_interest),
        ("totalAmount", totalAmount, principal + expected_interest),
        ("monthlyInterest", monthlyInterest, expected_interest / (time * 12)),
    ]
    for name, actual, expected in checks:
        got = round(actual, 2)
        exp = round(expected, 2)
        assert got == exp, f"{context} -> {name} expected {exp} but got {got}"
