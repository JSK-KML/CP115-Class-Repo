import pytest
import subprocess
import sys
import os

@pytest.fixture
def exercise_path():
    """Fixture to get the path to exercise6.py"""
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'exercise6.py')

def run_exercise(exercise_path, inputs):
    """Run exercise6.py with given inputs and return output"""
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

def extract_overtime_pay(output):
    """Extract overtime pay from output"""
    lines = output.strip().split('\n')
    if len(lines) < 1:
        pytest.fail(f"Expected at least 1 output line but got {len(lines)}: {lines}")
    
    return float(lines[-1].strip())

@pytest.mark.parametrize("position,overtime_hours,is_weekend,expected_pay", [
    ("Manager", 5, "No", 225.0),    # 5 * 30 * 1.5 = 225
    ("Supervisor", 10, "No", 320.0), # (8 * 20 * 1.5) + (2 * 20 * 2.0) = 240 + 80 = 320
    ("Staff", 5, "Yes", 137.5),    # (5 * 15 * 1.5) + (5 * 5) = 112.5 + 25 = 137.5
    ("Intern", 12, "No", 160.0),   # (8 * 8 * 1.5) + (4 * 8 * 2.0) = 96 + 64 = 160
])
def test_overtime_calculations(exercise_path, position, overtime_hours, is_weekend, expected_pay):
    """Test overtime pay calculations for different positions"""
    inputs = f"{position}\n{overtime_hours}\n{is_weekend}\n"
    output = run_exercise(exercise_path, inputs)
    
    overtime_pay = extract_overtime_pay(output)
    
    assert abs(overtime_pay - expected_pay) < 0.01, f"\nInput: {position}, {overtime_hours}hrs, Weekend={is_weekend}\nExpected: {expected_pay}, Got: {overtime_pay}"

def test_first_8_hours_overtime_rate(exercise_path):
    """Test that first 8 hours of overtime are paid at 1.5x rate"""
    inputs = "Staff\n8\nNo\n"  # Staff, 8 hours overtime, no weekend
    output = run_exercise(exercise_path, inputs)
    
    overtime_pay = extract_overtime_pay(output)
    expected_pay = 8 * 15 * 1.5  # 8 hours at 1.5x rate = 180
    
    assert abs(overtime_pay - expected_pay) < 0.01, f"\nInput: Staff, 8hrs, Weekend=No\nExpected: {expected_pay}, Got: {overtime_pay}"

def test_weekend_bonus(exercise_path):
    """Test weekend bonus of RM5/hour"""
    inputs = "Staff\n5\nYes\n"  # Staff, 5 hours overtime, weekend
    output = run_exercise(exercise_path, inputs)
    
    overtime_pay = extract_overtime_pay(output)
    base_overtime = 5 * 15 * 1.5  # 112.5
    weekend_bonus = 5 * 5  # 25
    expected_pay = base_overtime + weekend_bonus  # 137.5
    
    assert abs(overtime_pay - expected_pay) < 0.01, f"\nInput: Staff, 5hrs, Weekend=Yes\nExpected: {expected_pay}, Got: {overtime_pay}"