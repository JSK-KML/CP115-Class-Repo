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


def grade_filter(grades):
    total = 0.0
    count = 0
    for g in grades:
        if g < 0 or g > 100:
            continue
        total += g
        count += 1
    average = total / count if count > 0 else 0.0
    return count, average


CASES = [
    [80, 150, 70, -5, 90],
    [50, 60, 70],
    [100, 0, 50],
    [120, 130, 80],
    [90, 85, 95, 100],
    [40, 55, 65, 75],
    [101, 99, 100],
    [0, 50, 100],
    [25, 50, 75],
    [60, 60, 60, 60],
]


@pytest.mark.parametrize("grades", CASES)
def test_grade_filter(exercise_path, grades):
    context = f"input grades={grades}"
    inputs = "".join(f"{g}\n" for g in grades) + "-1\n"
    output = run_exercise(exercise_path, inputs)
    line1, line2 = read_lines(output, 2, context)

    exp_count, exp_avg = grade_filter(grades)

    assert line1 == str(exp_count), f"{context} -> valid count expected {exp_count} but got {line1!r}"
    assert round(float(line2), 2) == round(exp_avg, 2), f"{context} -> average expected {round(exp_avg, 2)} but got {line2!r}"
