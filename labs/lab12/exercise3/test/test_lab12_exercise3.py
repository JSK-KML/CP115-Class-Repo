import subprocess
import sys
import os

def run_exercise3(*inputs):
    """Run exercise3.py with given inputs and return output lines."""
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    script_path = os.path.join(script_dir, 'exercise3.py')

    input_data = '\n'.join(str(x) for x in inputs) + '\n'

    result = subprocess.run([sys.executable, script_path],
                          input=input_data, text=True, capture_output=True)

    if result.returncode != 0:
        raise Exception(f"Script failed: {result.stderr}")

    lines = result.stdout.strip().split('\n')
    return int(lines[0]), int(lines[1]), float(lines[2])

def test_single_age():
    """Test with single age"""
    ages = [25, "done"]
    inputs = ages
    age_count, total_age, average_age = run_exercise3(*inputs)
    assert age_count == 1, f"Input: {inputs} | Expected age_count: 1 | Got: {age_count}"
    assert total_age == 25, f"Input: {inputs} | Expected total_age: 25 | Got: {total_age}"
    assert average_age == 25.00, f"Input: {inputs} | Expected average_age: 25.00 | Got: {average_age}"

def test_multiple_ages():
    """Test with multiple ages"""
    ages = [18, 25, 30, 45, 60, "done"]
    inputs = ages
    age_count, total_age, average_age = run_exercise3(*inputs)
    assert age_count == 5, f"Input: {inputs} | Expected age_count: 5 | Got: {age_count}"
    assert total_age == 178, f"Input: {inputs} | Expected total_age: 178 | Got: {total_age}"
    assert average_age == 35.60, f"Input: {inputs} | Expected average_age: 35.60 | Got: {average_age}"

def test_done_immediately():
    """Test with 'done' immediately"""
    ages = ["done"]
    inputs = ages
    age_count, total_age, average_age = run_exercise3(*inputs)
    assert age_count == 0, f"Input: {inputs} | Expected age_count: 0 | Got: {age_count}"
    assert total_age == 0, f"Input: {inputs} | Expected total_age: 0 | Got: {total_age}"
    assert average_age == 0.00, f"Input: {inputs} | Expected average_age: 0.00 | Got: {average_age}"

def test_boundary_ages():
    """Test with boundary ages 1 and 120"""
    ages = [1, 120, 50, "done"]
    inputs = ages
    age_count, total_age, average_age = run_exercise3(*inputs)
    assert age_count == 3, f"Input: {inputs} | Expected age_count: 3 | Got: {age_count}"
    assert total_age == 171, f"Input: {inputs} | Expected total_age: 171 | Got: {total_age}"
    assert average_age == 57.00, f"Input: {inputs} | Expected average_age: 57.00 | Got: {average_age}"

def test_all_same_ages():
    """Test with all same ages"""
    ages = [40, 40, 40, 40, "done"]
    inputs = ages
    age_count, total_age, average_age = run_exercise3(*inputs)
    assert age_count == 4, f"Input: {inputs} | Expected age_count: 4 | Got: {age_count}"
    assert total_age == 160, f"Input: {inputs} | Expected total_age: 160 | Got: {total_age}"
    assert average_age == 40.00, f"Input: {inputs} | Expected average_age: 40.00 | Got: {average_age}"

def test_young_ages():
    """Test with young ages"""
    ages = [5, 10, 15, 20, "done"]
    inputs = ages
    age_count, total_age, average_age = run_exercise3(*inputs)
    assert age_count == 4, f"Input: {inputs} | Expected age_count: 4 | Got: {age_count}"
    assert total_age == 50, f"Input: {inputs} | Expected total_age: 50 | Got: {total_age}"
    assert average_age == 12.50, f"Input: {inputs} | Expected average_age: 12.50 | Got: {average_age}"

def test_elderly_ages():
    """Test with elderly ages"""
    ages = [80, 90, 100, 110, "done"]
    inputs = ages
    age_count, total_age, average_age = run_exercise3(*inputs)
    assert age_count == 4, f"Input: {inputs} | Expected age_count: 4 | Got: {age_count}"
    assert total_age == 380, f"Input: {inputs} | Expected total_age: 380 | Got: {total_age}"
    assert average_age == 95.00, f"Input: {inputs} | Expected average_age: 95.00 | Got: {average_age}"

def test_mixed_ages():
    """Test with mixed age range"""
    ages = [1, 30, 60, 90, 120, "done"]
    inputs = ages
    age_count, total_age, average_age = run_exercise3(*inputs)
    assert age_count == 5, f"Input: {inputs} | Expected age_count: 5 | Got: {age_count}"
    assert total_age == 301, f"Input: {inputs} | Expected total_age: 301 | Got: {total_age}"
    assert average_age == 60.20, f"Input: {inputs} | Expected average_age: 60.20 | Got: {average_age}"

def test_middle_ages():
    """Test with middle-age range"""
    ages = [35, 40, 45, 50, 55, "done"]
    inputs = ages
    age_count, total_age, average_age = run_exercise3(*inputs)
    assert age_count == 5, f"Input: {inputs} | Expected age_count: 5 | Got: {age_count}"
    assert total_age == 225, f"Input: {inputs} | Expected total_age: 225 | Got: {total_age}"
    assert average_age == 45.00, f"Input: {inputs} | Expected average_age: 45.00 | Got: {average_age}"

def test_many_ages():
    """Test with many ages"""
    ages = [20, 25, 30, 35, 40, 45, 50, 55, "done"]
    inputs = ages
    age_count, total_age, average_age = run_exercise3(*inputs)
    assert age_count == 8, f"Input: {inputs} | Expected age_count: 8 | Got: {age_count}"
    assert total_age == 300, f"Input: {inputs} | Expected total_age: 300 | Got: {total_age}"
    assert average_age == 37.50, f"Input: {inputs} | Expected average_age: 37.50 | Got: {average_age}"
