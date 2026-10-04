import pytest
import subprocess
import sys
import os


@pytest.fixture
def exercise_path():
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'exercise2.py')


def run_exercise(exercise_path, inputs):
    if not os.path.isfile(exercise_path):
        pytest.fail("exercise2.py was not found in the exercise2 folder")

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


def test_first_divisible(exercise_path):
    context = "no input"
    output = run_exercise(exercise_path, "")
    (line1,) = read_lines(output, 1, context)

    # The first number from 1 to 100 divisible by both 7 and 13 is 91.
    assert line1 == "91", f"{context} -> found number expected 91 but got {line1!r}"
