import pytest
import subprocess
import sys
import os


@pytest.fixture
def exercise_path():
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'exercise4.py')


def run_exercise(exercise_path, inputs):
    if not os.path.isfile(exercise_path):
        pytest.fail("exercise4.py was not found in the exercise4 folder")

    process = subprocess.Popen(
        [sys.executable, exercise_path],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    try:
        stdout, stderr = process.communicate(input=inputs, timeout=30)
    except subprocess.TimeoutExpired:
        process.kill()
        process.communicate()
        pytest.fail("the program took too long to finish (over 30 seconds) - check for an infinite loop")

    if process.returncode != 0:
        error = stderr.strip().splitlines()[-1] if stderr.strip() else "the program crashed"
        pytest.fail(f"the program did not run: {error}")

    return stdout


def read_lines(output, count, context):
    lines = output.replace("\r\n", "\n").strip().split('\n') if output.strip() else []
    if len(lines) != count:
        pytest.fail(
            f"{context}: expected {count} line(s) of output but got {len(lines)}. "
            f"Actual output: {output!r}"
        )
    return lines


def shrinking_queue(times):
    # Serve customers, add each one, then stop once total reaches 60.
    customers = 0
    total = 0
    for t in times:
        customers += 1
        total += t
        if total >= 60:
            break
    return customers, total


# Each case is the full list of service times entered; the program stops
# as soon as the running total reaches 60, so later values are ignored.
CASES = [
    [20, 25, 30, 10],
    [60],
    [30, 30],
    [10, 10, 10, 10, 10, 10],
    [59, 1],
    [100],
    [25, 25, 25],
    [15, 15, 15, 15, 5],
    [50, 20, 99],
    [40, 40],
]


@pytest.mark.parametrize("times", CASES)
def test_shrinking_queue(exercise_path, times):
    context = f"input times={times}"
    inputs = "".join(f"{t}\n" for t in times)
    output = run_exercise(exercise_path, inputs)
    line1, line2 = read_lines(output, 2, context)

    exp_customers, exp_total = shrinking_queue(times)

    assert line1 == str(exp_customers), f"{context} -> customers served expected {exp_customers} but got {line1!r}"
    assert line2 == str(exp_total), f"{context} -> minutes open expected {exp_total} but got {line2!r}"
