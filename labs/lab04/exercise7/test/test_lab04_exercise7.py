import pytest
import subprocess
import sys
import os


@pytest.fixture
def exercise_path():
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'lab-4-7.py')


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


def thermostat_power(tempRoom, tempTarget):
    if tempRoom < tempTarget:
        power = (tempTarget - tempRoom) * 10
    elif tempRoom > tempTarget:
        power = (tempRoom - tempTarget) * 8
    else:
        power = 0
    return min(power, 100)


@pytest.mark.parametrize("tempRoom,tempTarget", [
    (20, 25),
    (25, 20),
    (20, 20),
    (10, 25),
    (30, 10),
    (22, 25),
    (28, 25),
    (25, 35),
    (35, 25),
    (0, 0),
])
def test_thermostat_power(exercise_path, tempRoom, tempTarget):
    context = f"inputs tempRoom={tempRoom}, tempTarget={tempTarget}"
    inputs = f"{tempRoom}\n{tempTarget}\n"
    output = run_exercise(exercise_path, inputs)
    (result,) = read_numbers(output, 1, context)

    expected = round(thermostat_power(tempRoom, tempTarget), 2)
    got = round(result, 2)

    assert got == expected, f"{context} -> expected {expected} but got {got}"
