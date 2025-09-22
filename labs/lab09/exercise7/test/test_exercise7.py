import pytest
import subprocess
import sys
import os

@pytest.fixture
def exercise_path():
    """Fixture to get the path to exercise7.py"""
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'exercise7.py')

def run_exercise(exercise_path, inputs):
    """Run exercise7.py with given inputs and return output"""
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

def extract_admission_status(output):
    """Extract admission status from output"""
    lines = output.strip().split('\n')
    if len(lines) < 1:
        pytest.fail(f"Expected at least 1 output line but got {len(lines)}: {lines}")
    
    return lines[-1].strip()

@pytest.mark.parametrize("gpa,score,extracurricular,interview,expected_status", [
    # Accepted - All 4 requirements met
    (3.5, 1300, "2", "Yes", "Accepted"),
    (3.0, 1200, "1", "Yes", "Accepted"), 
    
    # Waitlisted - Exactly 3 requirements met
    (2.8, 1300, "2", "Yes", "Waitlisted"),  # Missing GPA
    (3.5, 1100, "2", "Yes", "Waitlisted"),  # Missing score
    (3.5, 1300, "0", "Yes", "Waitlisted"),  # Missing extracurricular
    
    # Rejected - Less than 3 requirements met
    (2.5, 1100, "0", "No", "Rejected"),     # Only 0 requirements met
    (3.5, 1300, "0", "No", "Rejected"),     # Only 2 requirements met
])
def test_admission_decisions(exercise_path, gpa, score, extracurricular, interview, expected_status):
    """Test college admission decisions based on requirements"""
    inputs = f"{gpa}\n{score}\n{extracurricular}\n{interview}\n"
    output = run_exercise(exercise_path, inputs)
    
    admission_status = extract_admission_status(output)
    
    assert admission_status == expected_status, f"\nInput: GPA={gpa}, Score={score}, Activities={extracurricular}, Interview={interview}\nExpected: {expected_status}, Got: {admission_status}"

def test_boundary_requirements(exercise_path):
    """Test boundary conditions for admission requirements"""
    # Exactly at boundaries should pass
    inputs = "3.0\n1200\n1\nYes\n"  # All minimum requirements
    output = run_exercise(exercise_path, inputs)
    status = extract_admission_status(output)
    assert status == "Accepted", f"\nInput: GPA=3.0, Score=1200, Activities=1, Interview=Yes\nExpected: Accepted, Got: {status}"
    
    # Just below boundaries should fail those requirements
    inputs = "2.9\n1199\n0\nNo\n"  # All below requirements
    output = run_exercise(exercise_path, inputs)
    status = extract_admission_status(output)
    assert status == "Rejected", f"\nInput: GPA=2.9, Score=1199, Activities=0, Interview=No\nExpected: Rejected, Got: {status}"