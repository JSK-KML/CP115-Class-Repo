import pytest
import subprocess
import sys
import os

@pytest.fixture
def exercise_path():
    """Fixture to get the path to exercise1.py"""
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'exercise1.py')

def run_exercise(exercise_path, inputs):
    """Run exercise1.py with given inputs and return output"""
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

@pytest.mark.parametrize("gpa,credits,expected_classification", [
    (3.9, 15, "Dean's List"),
    (3.6, 14, "Honor Roll"),
    (2.5, 12, "Good Standing"),
    (1.8, 12, "Academic Probation"),
    (3.8, 12, "Dean's List"),
    (3.5, 12, "Honor Roll"),
    (2.0, 15, "Good Standing"),
])
def test_student_classifications(exercise_path, gpa, credits, expected_classification):
    """Test various student classifications"""
    inputs = f"Test Student\n{gpa}\n{credits}\n"
    output = run_exercise(exercise_path, inputs)
    
    # Extract just the classification from the output
    lines = output.strip().split('\n')
    classification_line = [line for line in lines if "Classification:" in line][0]
    actual_classification = classification_line.split("Classification: ")[1]
    
    assert actual_classification == expected_classification, f"Expected '{expected_classification}' but got '{actual_classification}'"

@pytest.mark.parametrize("gpa,credits,expected_classification", [
    (3.9, 9, "Good Standing"),   # Part-time high GPA
    (3.6, 8, "Good Standing"),   # Part-time honor roll GPA  
    (1.5, 6, "Academic Probation"),  # Part-time low GPA
])
def test_part_time_students(exercise_path, gpa, credits, expected_classification):
    """Test that part-time students get correct classifications"""
    inputs = f"Test Student\n{gpa}\n{credits}\n"
    output = run_exercise(exercise_path, inputs)
    
    # Extract just the classification from the output
    lines = output.strip().split('\n')
    classification_line = [line for line in lines if "Classification:" in line][0]
    actual_classification = classification_line.split("Classification: ")[1]
    
    assert actual_classification == expected_classification, f"Expected '{expected_classification}' but got '{actual_classification}'"