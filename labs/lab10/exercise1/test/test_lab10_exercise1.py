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
    hourly_rate, overtime_pay, total_pay = run_exercise1("Manager", 8, "No")
    assert hourly_rate == 35, f"Expected 35 for hourly_rate but got {hourly_rate}"
    assert overtime_pay == 420, f"Expected 420 for overtime_pay but got {overtime_pay}"  # 8 * 35 * 1.5
    assert total_pay == 420, f"Expected 420 for total_pay but got {total_pay}"

def test_manager_weekend():
    """Manager, 5 hours overtime, weekend"""
    hourly_rate, overtime_pay, total_pay = run_exercise1("Manager", 5, "Yes")
    assert hourly_rate == 35, f"Expected 35 for hourly_rate but got {hourly_rate}"
    assert overtime_pay == 287, f"Expected 287 for overtime_pay but got {overtime_pay}"  # (5 * 35 * 1.5) + (5 * 5) = 262.5 + 25
    assert total_pay == 287, f"Expected 287 for total_pay but got {total_pay}"

def test_supervisor_weekday():
    """Supervisor, 10 hours overtime, weekday"""
    hourly_rate, overtime_pay, total_pay = run_exercise1("Supervisor", 10, "No")
    assert hourly_rate == 25, f"Expected 25 for hourly_rate but got {hourly_rate}"
    assert overtime_pay == 375, f"Expected 375 for overtime_pay but got {overtime_pay}"  # 10 * 25 * 1.5
    assert total_pay == 375, f"Expected 375 for total_pay but got {total_pay}"

def test_supervisor_weekend():
    """Supervisor, 6 hours overtime, weekend"""
    hourly_rate, overtime_pay, total_pay = run_exercise1("Supervisor", 6, "Yes")
    assert hourly_rate == 25, f"Expected 25 for hourly_rate but got {hourly_rate}"
    assert overtime_pay == 255, f"Expected 255 for overtime_pay but got {overtime_pay}"  # (6 * 25 * 1.5) + (6 * 5) = 225 + 30
    assert total_pay == 255, f"Expected 255 for total_pay but got {total_pay}"

def test_staff_weekday():
    """Staff, 12 hours overtime, weekday"""
    hourly_rate, overtime_pay, total_pay = run_exercise1("Staff", 12, "No")
    assert hourly_rate == 18, f"Expected 18 for hourly_rate but got {hourly_rate}"
    assert overtime_pay == 324, f"Expected 324 for overtime_pay but got {overtime_pay}"  # 12 * 18 * 1.5
    assert total_pay == 324, f"Expected 324 for total_pay but got {total_pay}"

def test_staff_weekend():
    """Staff, 4 hours overtime, weekend"""
    hourly_rate, overtime_pay, total_pay = run_exercise1("Staff", 4, "Yes")
    assert hourly_rate == 18, f"Expected 18 for hourly_rate but got {hourly_rate}"
    assert overtime_pay == 128, f"Expected 128 for overtime_pay but got {overtime_pay}"  # (4 * 18 * 1.5) + (4 * 5) = 108 + 20
    assert total_pay == 128, f"Expected 128 for total_pay but got {total_pay}"

def test_manager_no_overtime_weekday():
    """Manager, 0 hours overtime, weekday"""
    hourly_rate, overtime_pay, total_pay = run_exercise1("Manager", 0, "No")
    assert hourly_rate == 35, f"Expected 35 for hourly_rate but got {hourly_rate}"
    assert overtime_pay == 0, f"Expected 0 for overtime_pay but got {overtime_pay}"
    assert total_pay == 0, f"Expected 0 for total_pay but got {total_pay}"

def test_supervisor_large_overtime_weekend():
    """Supervisor, 15 hours overtime, weekend"""
    hourly_rate, overtime_pay, total_pay = run_exercise1("Supervisor", 15, "Yes")
    assert hourly_rate == 25, f"Expected 25 for hourly_rate but got {hourly_rate}"
    assert overtime_pay == 637, f"Expected 637 for overtime_pay but got {overtime_pay}"  # (15 * 25 * 1.5) + (15 * 5) = 562.5 + 75
    assert total_pay == 637, f"Expected 637 for total_pay but got {total_pay}"

def test_staff_single_hour_weekend():
    """Staff, 1 hour overtime, weekend"""
    hourly_rate, overtime_pay, total_pay = run_exercise1("Staff", 1, "Yes")
    assert hourly_rate == 18, f"Expected 18 for hourly_rate but got {hourly_rate}"
    assert overtime_pay == 32, f"Expected 32 for overtime_pay but got {overtime_pay}"  # (1 * 18 * 1.5) + (1 * 5) = 27 + 5
    assert total_pay == 32, f"Expected 32 for total_pay but got {total_pay}"

def test_manager_moderate_overtime_weekend():
    """Manager, 7 hours overtime, weekend"""
    hourly_rate, overtime_pay, total_pay = run_exercise1("Manager", 7, "Yes")
    assert hourly_rate == 35, f"Expected 35 for hourly_rate but got {hourly_rate}"
    assert overtime_pay == 402, f"Expected 402 for overtime_pay but got {overtime_pay}"  # (7 * 35 * 1.5) + (7 * 5) = 367.5 + 35
    assert total_pay == 402, f"Expected 402 for total_pay but got {total_pay}"