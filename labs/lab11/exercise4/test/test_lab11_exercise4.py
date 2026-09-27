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


def beat_the_record(sales_list):
    best = 0
    record_days = 0
    count = 0
    for s in sales_list:
        count += 1
        if s > best:
            record_days += 1
            best = s
    return count, record_days


CASES = [
    [30, 20, 50, 50, 80, 10],
    [5, 4, 3, 2, 1],
    [10, 20, 30],
    [40],
    [15, 15, 15],
    [100, 50, 200, 150, 300],
    [7, 8, 9, 6, 10],
    [25, 25, 26, 24, 27],
    [60, 10, 10, 10],
    [1, 2, 1, 3, 1, 4],
]


@pytest.mark.parametrize("sales_list", CASES)
def test_beat_the_record(exercise_path, sales_list):
    context = f"input sales={sales_list}"
    inputs = "".join(f"{s}\n" for s in sales_list) + "0\n"
    output = run_exercise(exercise_path, inputs)
    line1, line2 = read_lines(output, 2, context)

    exp_count, exp_records = beat_the_record(sales_list)

    assert line1 == str(exp_count), f"{context} -> total days expected {exp_count} but got {line1!r}"
    assert line2 == str(exp_records), f"{context} -> record days expected {exp_records} but got {line2!r}"
