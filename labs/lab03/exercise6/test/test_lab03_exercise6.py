import pytest
import subprocess
import sys
import os


@pytest.fixture
def exercise_path():
    """Path to the student's solution file."""
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'lab-03-6.py')


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


@pytest.mark.parametrize("yardLength,yardWidth,houseLength,houseWidth", [
    (10, 10, 5, 5),
    (20, 15, 10, 5),
    (8, 6, 4, 3),
    (100, 50, 20, 10),
    (12.5, 10, 5, 4),
    (30, 20, 10, 10),
    (7, 7, 3, 3),
    (50, 40, 25, 20),
    (15, 12, 6, 5),
    (9, 9, 4, 4),
])
def test_mow_yard(exercise_path, yardLength, yardWidth, houseLength, houseWidth):
    """wage = (yard area - house area) * RM2 per square metre. Inputs in order."""
    context = f"inputs yardLength={yardLength}, yardWidth={yardWidth}, houseLength={houseLength}, houseWidth={houseWidth}"
    inputs = f"{yardLength}\n{yardWidth}\n{houseLength}\n{houseWidth}\n"
    output = run_exercise(exercise_path, inputs)
    (result,) = read_numbers(output, 1, context)

    expected = round((yardLength * yardWidth - houseLength * houseWidth) * 2.00, 2)
    got = round(result, 2)

    assert got == expected, f"{context} -> expected {expected} but got {got}"
