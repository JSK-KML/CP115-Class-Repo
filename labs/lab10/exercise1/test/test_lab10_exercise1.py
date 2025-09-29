import subprocess
import sys
import os

def run_exercise1(position, overtime_hours, is_weekend):
    """Run exercise1.py with given inputs and return output lines."""
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    script_path = os.path.join(script_dir, 'exercise1.py')

    input_data = f"{position}\n{overtime_hours}\n{is_weekend}\n"

    result = subprocess.run([sys.executable, script_path],
                          input=input_data, text=True, capture_output=True)

    if result.returncode != 0:
        raise Exception(f"Script failed: {result.stderr}")

    lines = result.stdout.strip().split('\n')
    return [int(float(line)) for line in lines]

def test_manager_weekday():
    """Manager, 8 hours overtime, weekday"""
    position, overtime_hours, is_weekend = "Manager", 8, "No"
    inputs = f"position='{position}', overtime_hours={overtime_hours}, is_weekend='{is_weekend}'"
    hourly_rate, overtime_pay, total_pay = run_exercise1(position, overtime_hours, is_weekend)
    assert hourly_rate == 35, f"Input: {inputs} | Expected hourly_rate: 35 | Got: {hourly_rate}"
    assert overtime_pay == 420, f"Input: {inputs} | Expected overtime_pay: 420 | Got: {overtime_pay}"  # 8 * 35 * 1.5
    assert total_pay == 420, f"Input: {inputs} | Expected total_pay: 420 | Got: {total_pay}"

def test_manager_weekend():
    """Manager, 5 hours overtime, weekend"""
    position, overtime_hours, is_weekend = "Manager", 5, "Yes"
    inputs = f"position='{position}', overtime_hours={overtime_hours}, is_weekend='{is_weekend}'"
    hourly_rate, overtime_pay, total_pay = run_exercise1(position, overtime_hours, is_weekend)
    assert hourly_rate == 35, f"Input: {inputs} | Expected hourly_rate: 35 | Got: {hourly_rate}"
    assert overtime_pay == 292, f"Input: {inputs} | Expected overtime_pay: 292 | Got: {overtime_pay}"  # (5 * 35 * 1.5) + (5 * 6) = 262.5 + 30
    assert total_pay == 292, f"Input: {inputs} | Expected total_pay: 292 | Got: {total_pay}"

def test_supervisor_weekday():
    """Supervisor, 10 hours overtime, weekday"""
    position, overtime_hours, is_weekend = "Supervisor", 10, "No"
    inputs = f"position='{position}', overtime_hours={overtime_hours}, is_weekend='{is_weekend}'"
    hourly_rate, overtime_pay, total_pay = run_exercise1(position, overtime_hours, is_weekend)
    assert hourly_rate == 25, f"Input: {inputs} | Expected hourly_rate: 25 | Got: {hourly_rate}"
    assert overtime_pay == 375, f"Input: {inputs} | Expected overtime_pay: 375 | Got: {overtime_pay}"  # 10 * 25 * 1.5
    assert total_pay == 375, f"Input: {inputs} | Expected total_pay: 375 | Got: {total_pay}"

def test_supervisor_weekend():
    """Supervisor, 6 hours overtime, weekend"""
    position, overtime_hours, is_weekend = "Supervisor", 6, "Yes"
    inputs = f"position='{position}', overtime_hours={overtime_hours}, is_weekend='{is_weekend}'"
    hourly_rate, overtime_pay, total_pay = run_exercise1(position, overtime_hours, is_weekend)
    assert hourly_rate == 25, f"Input: {inputs} | Expected hourly_rate: 25 | Got: {hourly_rate}"
    assert overtime_pay == 261, f"Input: {inputs} | Expected overtime_pay: 261 | Got: {overtime_pay}"  # (6 * 25 * 1.5) + (6 * 6) = 225 + 36
    assert total_pay == 261, f"Input: {inputs} | Expected total_pay: 261 | Got: {total_pay}"

def test_staff_weekday():
    """Staff, 12 hours overtime, weekday"""
    position, overtime_hours, is_weekend = "Staff", 12, "No"
    inputs = f"position='{position}', overtime_hours={overtime_hours}, is_weekend='{is_weekend}'"
    hourly_rate, overtime_pay, total_pay = run_exercise1(position, overtime_hours, is_weekend)
    assert hourly_rate == 18, f"Input: {inputs} | Expected hourly_rate: 18 | Got: {hourly_rate}"
    assert overtime_pay == 324, f"Input: {inputs} | Expected overtime_pay: 324 | Got: {overtime_pay}"  # 12 * 18 * 1.5
    assert total_pay == 324, f"Input: {inputs} | Expected total_pay: 324 | Got: {total_pay}"

def test_staff_weekend():
    """Staff, 4 hours overtime, weekend"""
    position, overtime_hours, is_weekend = "Staff", 4, "Yes"
    inputs = f"position='{position}', overtime_hours={overtime_hours}, is_weekend='{is_weekend}'"
    hourly_rate, overtime_pay, total_pay = run_exercise1(position, overtime_hours, is_weekend)
    assert hourly_rate == 18, f"Input: {inputs} | Expected hourly_rate: 18 | Got: {hourly_rate}"
    assert overtime_pay == 132, f"Input: {inputs} | Expected overtime_pay: 132 | Got: {overtime_pay}"  # (4 * 18 * 1.5) + (4 * 6) = 108 + 24
    assert total_pay == 132, f"Input: {inputs} | Expected total_pay: 132 | Got: {total_pay}"

def test_manager_no_overtime_weekday():
    """Manager, 0 hours overtime, weekday"""
    position, overtime_hours, is_weekend = "Manager", 0, "No"
    inputs = f"position='{position}', overtime_hours={overtime_hours}, is_weekend='{is_weekend}'"
    hourly_rate, overtime_pay, total_pay = run_exercise1(position, overtime_hours, is_weekend)
    assert hourly_rate == 35, f"Input: {inputs} | Expected hourly_rate: 35 | Got: {hourly_rate}"
    assert overtime_pay == 0, f"Input: {inputs} | Expected overtime_pay: 0 | Got: {overtime_pay}"
    assert total_pay == 0, f"Input: {inputs} | Expected total_pay: 0 | Got: {total_pay}"

def test_supervisor_large_overtime_weekend():
    """Supervisor, 15 hours overtime, weekend"""
    position, overtime_hours, is_weekend = "Supervisor", 15, "Yes"
    inputs = f"position='{position}', overtime_hours={overtime_hours}, is_weekend='{is_weekend}'"
    hourly_rate, overtime_pay, total_pay = run_exercise1(position, overtime_hours, is_weekend)
    assert hourly_rate == 25, f"Input: {inputs} | Expected hourly_rate: 25 | Got: {hourly_rate}"
    assert overtime_pay == 652, f"Input: {inputs} | Expected overtime_pay: 652 | Got: {overtime_pay}"  # (15 * 25 * 1.5) + (15 * 6) = 562.5 + 90
    assert total_pay == 652, f"Input: {inputs} | Expected total_pay: 652 | Got: {total_pay}"

def test_staff_single_hour_weekend():
    """Staff, 1 hour overtime, weekend"""
    position, overtime_hours, is_weekend = "Staff", 1, "Yes"
    inputs = f"position='{position}', overtime_hours={overtime_hours}, is_weekend='{is_weekend}'"
    hourly_rate, overtime_pay, total_pay = run_exercise1(position, overtime_hours, is_weekend)
    assert hourly_rate == 18, f"Input: {inputs} | Expected hourly_rate: 18 | Got: {hourly_rate}"
    assert overtime_pay == 33, f"Input: {inputs} | Expected overtime_pay: 33 | Got: {overtime_pay}"  # (1 * 18 * 1.5) + (1 * 6) = 27 + 6
    assert total_pay == 33, f"Input: {inputs} | Expected total_pay: 33 | Got: {total_pay}"

def test_manager_moderate_overtime_weekend():
    """Manager, 7 hours overtime, weekend"""
    position, overtime_hours, is_weekend = "Manager", 7, "Yes"
    inputs = f"position='{position}', overtime_hours={overtime_hours}, is_weekend='{is_weekend}'"
    hourly_rate, overtime_pay, total_pay = run_exercise1(position, overtime_hours, is_weekend)
    assert hourly_rate == 35, f"Input: {inputs} | Expected hourly_rate: 35 | Got: {hourly_rate}"
    assert overtime_pay == 409, f"Input: {inputs} | Expected overtime_pay: 409 | Got: {overtime_pay}"  # (7 * 35 * 1.5) + (7 * 6) = 367.5 + 42
    assert total_pay == 409, f"Input: {inputs} | Expected total_pay: 409 | Got: {total_pay}"