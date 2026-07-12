import pytest
import subprocess
import sys
import os


@pytest.fixture
def exercise_path():
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'lab-4-9.py')


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


def cheaper_plan(gb):
    plan_a = 10.0 + gb * 1.0
    plan_b = 25.0 + max(0, gb - 20) * 3.0
    return min(plan_a, plan_b)


@pytest.mark.parametrize("gb", [0, 5, 15, 20, 25, 30, 10, 18, 40, 22])
def test_cheaper_plan(exercise_path, gb):
    context = f"input gb={gb}"
    output = run_exercise(exercise_path, f"{gb}\n")
    (result,) = read_numbers(output, 1, context)

    expected = round(cheaper_plan(gb), 2)
    got = round(result, 2)

    assert got == expected, f"{context} -> expected {expected} but got {got}"
