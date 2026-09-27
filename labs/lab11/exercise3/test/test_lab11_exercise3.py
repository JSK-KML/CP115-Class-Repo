import pytest
import subprocess
import sys
import os


@pytest.fixture
def exercise_path():
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'exercise3.py')


def run_exercise(exercise_path, inputs):
    if not os.path.isfile(exercise_path):
        pytest.fail("exercise3.py was not found in the exercise3 folder")

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


def read_lines(output, count, context):
    lines = output.replace("\r\n", "\n").strip().split('\n') if output.strip() else []
    if len(lines) != count:
        pytest.fail(
            f"{context}: expected {count} line(s) of output but got {len(lines)}. "
            f"Actual output: {output!r}"
        )
    return lines


def biggest_jump(numbers):
    # numbers has at least one value (the primed first reading).
    previous = numbers[0]
    biggest = 0
    count = 1
    for n in numbers[1:]:
        count += 1
        jump = n - previous
        if jump > biggest:
            biggest = jump
        previous = n
    return count, biggest


CASES = [
    [5, 9, 7, 20, 3],
    [10, 20, 30],
    [30, 20, 10],
    [5, 5, 5],
    [1, 100],
    [40],
    [7, 8, 6, 15, 15, 40],
    [50, 10, 60, 20, 90],
    [2, 3, 1, 4, 1, 5],
    [10, 10, 25],
]


@pytest.mark.parametrize("numbers", CASES)
def test_biggest_jump(exercise_path, numbers):
    context = f"input numbers={numbers}"
    inputs = "".join(f"{n}\n" for n in numbers) + "0\n"
    output = run_exercise(exercise_path, inputs)
    line1, line2 = read_lines(output, 2, context)

    exp_count, exp_jump = biggest_jump(numbers)

    assert line1 == str(exp_count), f"{context} -> total readings expected {exp_count} but got {line1!r}"
    assert line2 == str(exp_jump), f"{context} -> biggest jump expected {exp_jump} but got {line2!r}"
