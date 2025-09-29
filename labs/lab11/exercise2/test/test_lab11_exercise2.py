import subprocess
import sys
import os

def run_exercise2(*inputs):
    """Run exercise2.py with given inputs and return output lines."""
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    script_path = os.path.join(script_dir, 'exercise2.py')

    input_data = '\n'.join(str(x) for x in inputs) + '\n'

    result = subprocess.run([sys.executable, script_path],
                          input=input_data, text=True, capture_output=True)

    if result.returncode != 0:
        raise Exception(f"Script failed: {result.stderr}")

    lines = result.stdout.strip().split('\n')
    return int(lines[0]), float(lines[1])

def test_no_danger_days():
    """Test temperatures all below threshold"""
    num_days = 3
    danger_threshold = 35.0
    temperatures = [30.0, 32.5, 34.9]
    inputs = [num_days, danger_threshold] + temperatures
    danger_days, average_temp = run_exercise2(*inputs)
    expected_danger_days = 0
    expected_average = 32.5  # (30 + 32.5 + 34.9) / 3 = 97.4 / 3
    assert danger_days == expected_danger_days, f"Expected danger_days: {expected_danger_days} | Got: {danger_days}"
    assert abs(average_temp - expected_average) < 0.1, f"Expected average_temp: {expected_average} | Got: {average_temp}"

def test_all_danger_days():
    """Test temperatures all above threshold"""
    num_days = 3
    danger_threshold = 30.0
    temperatures = [35.0, 37.5, 40.0]
    inputs = [num_days, danger_threshold] + temperatures
    danger_days, average_temp = run_exercise2(*inputs)
    expected_danger_days = 3
    expected_average = 37.5  # (35 + 37.5 + 40) / 3 = 112.5 / 3
    assert danger_days == expected_danger_days, f"Expected danger_days: {expected_danger_days} | Got: {danger_days}"
    assert abs(average_temp - expected_average) < 0.1, f"Expected average_temp: {expected_average} | Got: {average_temp}"

def test_mixed_danger_days():
    """Test mix of danger and safe temperatures"""
    num_days = 4
    danger_threshold = 35.0
    temperatures = [32.0, 37.0, 34.0, 39.0]
    inputs = [num_days, danger_threshold] + temperatures
    danger_days, average_temp = run_exercise2(*inputs)
    expected_danger_days = 2  # 37.0 and 39.0 are above 35.0
    expected_average = 35.5  # (32 + 37 + 34 + 39) / 4 = 142 / 4
    assert danger_days == expected_danger_days, f"Expected danger_days: {expected_danger_days} | Got: {danger_days}"
    assert abs(average_temp - expected_average) < 0.1, f"Expected average_temp: {expected_average} | Got: {average_temp}"

def test_single_day():
    """Test single day above threshold"""
    num_days = 1
    danger_threshold = 30.0
    temperatures = [35.5]
    inputs = [num_days, danger_threshold] + temperatures
    danger_days, average_temp = run_exercise2(*inputs)
    expected_danger_days = 1
    expected_average = 35.5
    assert danger_days == expected_danger_days, f"Expected danger_days: {expected_danger_days} | Got: {danger_days}"
    assert abs(average_temp - expected_average) < 0.1, f"Expected average_temp: {expected_average} | Got: {average_temp}"

def test_single_day_safe():
    """Test single day below threshold"""
    num_days = 1
    danger_threshold = 40.0
    temperatures = [25.0]
    inputs = [num_days, danger_threshold] + temperatures
    danger_days, average_temp = run_exercise2(*inputs)
    expected_danger_days = 0
    expected_average = 25.0
    assert danger_days == expected_danger_days, f"Expected danger_days: {expected_danger_days} | Got: {danger_days}"
    assert abs(average_temp - expected_average) < 0.1, f"Expected average_temp: {expected_average} | Got: {average_temp}"

def test_edge_case_exact_threshold():
    """Test temperature exactly at threshold (should not count as danger)"""
    num_days = 3
    danger_threshold = 35.0
    temperatures = [34.9, 35.0, 35.1]
    inputs = [num_days, danger_threshold] + temperatures
    danger_days, average_temp = run_exercise2(*inputs)
    expected_danger_days = 1  # Only 35.1 is above 35.0
    expected_average = 35.0  # (34.9 + 35.0 + 35.1) / 3 = 105 / 3
    assert danger_days == expected_danger_days, f"Expected danger_days: {expected_danger_days} | Got: {danger_days}"
    assert abs(average_temp - expected_average) < 0.1, f"Expected average_temp: {expected_average} | Got: {average_temp}"

def test_extreme_temperatures():
    """Test very high and very low temperatures"""
    num_days = 4
    danger_threshold = 25.0
    temperatures = [10.0, 50.0, 5.0, 45.0]
    inputs = [num_days, danger_threshold] + temperatures
    danger_days, average_temp = run_exercise2(*inputs)
    expected_danger_days = 2  # 50.0 and 45.0 are above 25.0
    expected_average = 27.5  # (10 + 50 + 5 + 45) / 4 = 110 / 4
    assert danger_days == expected_danger_days, f"Expected danger_days: {expected_danger_days} | Got: {danger_days}"
    assert abs(average_temp - expected_average) < 0.1, f"Expected average_temp: {expected_average} | Got: {average_temp}"

def test_many_days():
    """Test with many days"""
    num_days = 7
    danger_threshold = 30.0
    temperatures = [25.0, 32.0, 28.0, 35.0, 29.0, 38.0, 31.0]
    inputs = [num_days, danger_threshold] + temperatures
    danger_days, average_temp = run_exercise2(*inputs)
    expected_danger_days = 4  # 32.0, 35.0, 38.0, 31.0 are above 30.0
    expected_average = 31.1  # (25 + 32 + 28 + 35 + 29 + 38 + 31) / 7 = 218 / 7
    assert danger_days == expected_danger_days, f"Expected danger_days: {expected_danger_days} | Got: {danger_days}"
    assert abs(average_temp - expected_average) < 0.1, f"Expected average_temp: {expected_average} | Got: {average_temp}"

def test_high_threshold():
    """Test with very high threshold"""
    num_days = 4
    danger_threshold = 50.0
    temperatures = [40.0, 45.0, 35.0, 55.0]
    inputs = [num_days, danger_threshold] + temperatures
    danger_days, average_temp = run_exercise2(*inputs)
    expected_danger_days = 1  # Only 55.0 is above 50.0
    expected_average = 43.8  # (40 + 45 + 35 + 55) / 4 = 175 / 4
    assert danger_days == expected_danger_days, f"Expected danger_days: {expected_danger_days} | Got: {danger_days}"
    assert abs(average_temp - expected_average) < 0.1, f"Expected average_temp: {expected_average} | Got: {average_temp}"

def test_decimal_temperatures():
    """Test with decimal temperatures"""
    num_days = 5
    danger_threshold = 33.5
    temperatures = [32.1, 34.7, 33.5, 35.9, 31.8]
    inputs = [num_days, danger_threshold] + temperatures
    danger_days, average_temp = run_exercise2(*inputs)
    expected_danger_days = 2  # 34.7 and 35.9 are above 33.5
    expected_average = 33.6  # (32.1 + 34.7 + 33.5 + 35.9 + 31.8) / 5 = 168 / 5
    assert danger_days == expected_danger_days, f"Expected danger_days: {expected_danger_days} | Got: {danger_days}"
    assert abs(average_temp - expected_average) < 0.1, f"Expected average_temp: {expected_average} | Got: {average_temp}"