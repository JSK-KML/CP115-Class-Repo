import pytest
import subprocess
import sys
import os


@pytest.fixture
def exercise_path():
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'exercise1.py')


def run_exercise(exercise_path, inputs):
    if not os.path.isfile(exercise_path):
        pytest.fail("exercise1.py was not found in the exercise1 folder")

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


def password_system(attempts):
    # Up to 3 attempts; stop as soon as the correct one is entered.
    used = 0
    success = False
    for guess in attempts[:3]:
        used += 1
        if guess == "python123":
            success = True
            break
    return success, used


CASES = [
    ["python123"],
    ["apple", "python123"],
    ["a", "b", "python123"],
    ["a", "b", "c"],
    ["Python123", "python123"],
    ["wrong", "wrong", "wrong"],
    ["python123", "wrong", "wrong"],
    ["x", "python123", "y"],
    ["123", "abc", "python"],
    ["python1234", "python123"],
]


@pytest.mark.parametrize("attempts", CASES)
def test_password_system(exercise_path, attempts):
    context = f"input attempts={attempts}"
    inputs = "".join(f"{a}\n" for a in attempts)
    output = run_exercise(exercise_path, inputs)
    line1, line2 = read_lines(output, 2, context)

    exp_success, exp_used = password_system(attempts)

    assert line1 == str(exp_success), f"{context} -> login success expected {exp_success} but got {line1!r}"
    assert line2 == str(exp_used), f"{context} -> attempts used expected {exp_used} but got {line2!r}"
