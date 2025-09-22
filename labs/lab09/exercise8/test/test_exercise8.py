import pytest
import subprocess
import sys
import os

@pytest.fixture
def exercise_path():
    """Fixture to get the path to exercise8.py"""
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'exercise8.py')

def run_exercise(exercise_path, inputs):
    """Run exercise8.py with given inputs and return output"""
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

def extract_approval_status(output):
    """Extract approval status from output"""
    lines = output.strip().split('\n')
    if len(lines) < 1:
        pytest.fail(f"Expected at least 1 output line but got {len(lines)}: {lines}")
    
    return lines[-1].strip()

@pytest.mark.parametrize("income,employment,credit,years,expected_status", [
    # Approved - All 4 criteria met
    (5000, "permanent", "excellent", 3, "Approved"),
    (3000, "contract", "good", 2, "Approved"),
    
    # Conditionally Approved - Exactly 3 criteria met
    (2500, "permanent", "excellent", 3, "Conditionally Approved"),  # Missing income
    (5000, "temporary", "excellent", 3, "Conditionally Approved"),  # Missing employment
    (5000, "permanent", "poor", 3, "Conditionally Approved"),      # Missing credit
    
    # Rejected - Less than 3 criteria met
    (2000, "temporary", "poor", 1, "Rejected"),        # 0 criteria met
    (5000, "permanent", "poor", 1, "Rejected"),        # Only 2 criteria met
])
def test_loan_approval_decisions(exercise_path, income, employment, credit, years, expected_status):
    """Test loan approval decisions based on criteria"""
    inputs = f"{income}\n{employment}\n{credit}\n{years}\n"
    output = run_exercise(exercise_path, inputs)
    
    approval_status = extract_approval_status(output)
    
    assert approval_status == expected_status, f"\nInput: Income={income}, Employment={employment}, Credit={credit}, Years={years}\nExpected: {expected_status}, Got: {approval_status}"

def test_income_boundary(exercise_path):
    """Test income requirement at boundary (RM3000)"""
    # Exactly RM3000 should meet requirement
    inputs = "3000\npermanent\nexcellent\n3\n"
    output = run_exercise(exercise_path, inputs)
    status = extract_approval_status(output)
    assert status == "Approved", f"\nInput: Income=3000, Employment=permanent, Credit=excellent, Years=3\nExpected: Approved, Got: {status}"
    
    # Below RM3000 should not meet requirement
    inputs = "2999\npermanent\nexcellent\n3\n"
    output = run_exercise(exercise_path, inputs)
    status = extract_approval_status(output)
    assert status == "Conditionally Approved", f"\nInput: Income=2999, Employment=permanent, Credit=excellent, Years=3\nExpected: Conditionally Approved, Got: {status}"