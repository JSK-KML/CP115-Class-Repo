import pytest
import subprocess
import sys
import os

@pytest.fixture
def exercise_path():
    """Fixture to get the path to exercise9.py"""
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'exercise9.py')

def run_exercise(exercise_path, inputs):
    """Run exercise9.py with given inputs and return output"""
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

def extract_license_class(output):
    """Extract license class from output"""
    lines = output.strip().split('\n')
    if len(lines) < 1:
        pytest.fail(f"Expected at least 1 output line but got {len(lines)}: {lines}")
    
    return lines[-1].strip()

@pytest.mark.parametrize("age,vision,written,driving,medical,expected_class", [
    # Class A (Commercial) - All 5 requirements + age 21+
    (25, "Pass", 85, 90, "Pass", "Class A (Commercial)"),
    (21, "Pass", 80, 85, "Pass", "Class A (Commercial)"),
    
    # Class B (Regular) - First 4 requirements + age 18+
    (20, "Pass", 85, 90, "Fail", "Class B (Regular)"),
    (18, "Pass", 80, 85, "Fail", "Class B (Regular)"),
    
    # Restricted License - 2-3 requirements met
    (25, "Pass", 85, 75, "Pass", "Restricted License"),  # Missing driving test
    (16, "Pass", 85, 90, "Pass", "Restricted License"),  # Age too young
    
    # Application Denied - Less than 2 requirements met
    (16, "Fail", 70, 75, "Fail", "Application Denied"),  # Only 0-1 requirements
])
def test_license_classification(exercise_path, age, vision, written, driving, medical, expected_class):
    """Test driver license classification based on requirements"""
    inputs = f"{age}\n{vision}\n{written}\n{driving}\n{medical}\n"
    output = run_exercise(exercise_path, inputs)
    
    license_class = extract_license_class(output)
    
    assert license_class == expected_class, f"\nInput: Age={age}, Vision={vision}, Written={written}, Driving={driving}, Medical={medical}\nExpected: {expected_class}, Got: {license_class}"

def test_age_requirements(exercise_path):
    """Test age requirements for different license classes"""
    # Age 21+ with all requirements = Class A
    inputs = "21\nPass\n80\n85\nPass\n"
    output = run_exercise(exercise_path, inputs)
    license_class = extract_license_class(output)
    assert license_class == "Class A (Commercial)", f"\nInput: Age=21, Vision=Pass, Written=80, Driving=85, Medical=Pass\nExpected: Class A (Commercial), Got: {license_class}"
    
    # Age 18-20 with first 4 requirements = Class B
    inputs = "20\nPass\n80\n85\nFail\n"
    output = run_exercise(exercise_path, inputs)
    license_class = extract_license_class(output)
    assert license_class == "Class B (Regular)", f"\nInput: Age=20, Vision=Pass, Written=80, Driving=85, Medical=Fail\nExpected: Class B (Regular), Got: {license_class}"

def test_test_score_boundaries(exercise_path):
    """Test written and driving test score boundaries"""
    # Exactly at boundaries should pass
    inputs = "25\nPass\n80\n85\nPass\n"
    output = run_exercise(exercise_path, inputs)
    license_class = extract_license_class(output)
    assert license_class == "Class A (Commercial)", f"\nInput: Age=25, Vision=Pass, Written=80, Driving=85, Medical=Pass\nExpected: Class A (Commercial), Got: {license_class}"
    
    # Below boundaries should fail
    inputs = "25\nPass\n79\n84\nPass\n"
    output = run_exercise(exercise_path, inputs)
    license_class = extract_license_class(output)
    assert license_class == "Restricted License", f"\nInput: Age=25, Vision=Pass, Written=79, Driving=84, Medical=Pass\nExpected: Restricted License, Got: {license_class}"