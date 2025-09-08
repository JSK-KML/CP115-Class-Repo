import pytest
import subprocess
import sys
import os

@pytest.fixture
def exercise_path():
    """Fixture to get the path to exercise4.py"""
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'exercise4.py')

def run_exercise(exercise_path, inputs):
    """Run exercise4.py with given inputs and return output"""
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

def extract_results(output):
    """Extract consumption, water cost, and total bill from output"""
    lines = output.strip().split('\n')
    if len(lines) < 3:
        pytest.fail(f"Expected 3 output lines but got {len(lines)}: {lines}")
    
    consumption = int(lines[0].strip())
    water_cost = float(lines[1].strip())
    total_bill = float(lines[2].strip())
    
    return consumption, water_cost, total_bill

@pytest.mark.parametrize("current,previous,expected_consumption,expected_water_cost,expected_total", [
    # Tier 1 only (≤20 cubic meters) - RM0.57 per cubic meter
    (1020, 1000, 20, 11.40, 21.40),    # 20 * 0.57 = 11.40, + 8 + 2 = 21.40
    (1015, 1000, 15, 8.55, 18.55),     # 15 * 0.57 = 8.55, + 8 + 2 = 18.55
    (1010, 1000, 10, 5.70, 15.70),     # 10 * 0.57 = 5.70, + 8 + 2 = 15.70
    (1005, 1000, 5, 2.85, 12.85),      # 5 * 0.57 = 2.85, + 8 + 2 = 12.85
    
    # Tier 1 + Tier 2 (21-35 cubic meters) - First 20 at RM0.57, next at RM1.03
    (1025, 1000, 25, 16.55, 26.55),    # (20*0.57) + (5*1.03) = 11.40 + 5.15 = 16.55, + 10 = 26.55
    (1030, 1000, 30, 21.70, 31.70),    # (20*0.57) + (10*1.03) = 11.40 + 10.30 = 21.70, + 10 = 31.70
    (1035, 1000, 35, 26.85, 36.85),    # (20*0.57) + (15*1.03) = 11.40 + 15.45 = 26.85, + 10 = 36.85
    
    # All three tiers (>35 cubic meters) - First 20 at RM0.57, next 15 at RM1.03, rest at RM1.40
    (1040, 1000, 40, 33.85, 43.85),    # (20*0.57) + (15*1.03) + (5*1.40) = 11.40 + 15.45 + 7.00 = 33.85, + 10 = 43.85
    (1050, 1000, 50, 47.85, 57.85),    # (20*0.57) + (15*1.03) + (15*1.40) = 11.40 + 15.45 + 21.00 = 47.85, + 10 = 57.85
    (1100, 1000, 100, 117.85, 127.85), # (20*0.57) + (15*1.03) + (65*1.40) = 11.40 + 15.45 + 91.00 = 117.85, + 10 = 127.85
])
def test_water_bill_calculations(exercise_path, current, previous, expected_consumption, expected_water_cost, expected_total):
    """Test various water bill calculation scenarios"""
    inputs = f"{current}\n{previous}\n"
    output = run_exercise(exercise_path, inputs)
    
    consumption, water_cost, total_bill = extract_results(output)
    
    assert consumption == expected_consumption, f"Expected consumption {expected_consumption} but got {consumption}"
    assert abs(water_cost - expected_water_cost) < 0.01, f"Expected water cost {expected_water_cost} but got {water_cost}"
    assert abs(total_bill - expected_total) < 0.01, f"Expected total bill {expected_total} but got {total_bill}"

@pytest.mark.parametrize("consumption,expected_water_cost", [
    # Boundary tests for tier transitions
    (20, 11.40),   # Last value in tier 1: 20 * 0.57 = 11.40
    (21, 12.43),   # First value in tier 2: (20 * 0.57) + (1 * 1.03) = 11.40 + 1.03 = 12.43
    (35, 26.85),   # Last value in tier 2: (20 * 0.57) + (15 * 1.03) = 11.40 + 15.45 = 26.85
    (36, 28.25),   # First value in tier 3: (20 * 0.57) + (15 * 1.03) + (1 * 1.40) = 26.85 + 1.40 = 28.25
])
def test_tier_boundaries(exercise_path, consumption, expected_water_cost):
    """Test water cost calculations at tier boundaries"""
    current = 1000 + consumption
    previous = 1000
    
    inputs = f"{current}\n{previous}\n"
    output = run_exercise(exercise_path, inputs)
    
    actual_consumption, actual_water_cost, _ = extract_results(output)
    
    assert actual_consumption == consumption, f"Expected consumption {consumption} but got {actual_consumption}"
    assert abs(actual_water_cost - expected_water_cost) < 0.01, f"Expected water cost {expected_water_cost} but got {actual_water_cost}"

def test_zero_consumption(exercise_path):
    """Test zero water consumption"""
    inputs = "1000\n1000\n"
    output = run_exercise(exercise_path, inputs)
    
    consumption, water_cost, total_bill = extract_results(output)
    
    assert consumption == 0, f"Expected consumption 0 but got {consumption}"
    assert water_cost == 0.0, f"Expected water cost 0.0 but got {water_cost}"
    assert total_bill == 10.0, f"Expected total bill 10.0 (service charges only) but got {total_bill}"

def test_service_charges_applied(exercise_path):
    """Test that service charge (RM8) and sewerage (RM2) are always applied"""
    inputs = "1001\n1000\n"  # 1 cubic meter consumption
    output = run_exercise(exercise_path, inputs)
    
    consumption, water_cost, total_bill = extract_results(output)
    
    assert consumption == 1, "Expected consumption 1"
    expected_water_cost = 1 * 0.57  # 0.57
    expected_total = expected_water_cost + 8 + 2  # 0.57 + 10 = 10.57
    
    assert abs(water_cost - expected_water_cost) < 0.01, f"Expected water cost {expected_water_cost} but got {water_cost}"
    assert abs(total_bill - expected_total) < 0.01, f"Expected total bill {expected_total} but got {total_bill}"

def test_large_consumption(exercise_path):
    """Test calculation with very large water consumption"""
    inputs = "1500\n1000\n"  # 500 cubic meters
    output = run_exercise(exercise_path, inputs)
    
    consumption, water_cost, total_bill = extract_results(output)
    
    assert consumption == 500, "Expected consumption 500"
    
    # Calculate expected cost: (20*0.57) + (15*1.03) + (465*1.40)
    expected_water_cost = (20 * 0.57) + (15 * 1.03) + (465 * 1.40)
    expected_water_cost = 11.40 + 15.45 + 651.00  # = 677.85
    expected_total = expected_water_cost + 10  # 687.85
    
    assert abs(water_cost - expected_water_cost) < 0.01, f"Expected water cost {expected_water_cost} but got {water_cost}"
    assert abs(total_bill - expected_total) < 0.01, f"Expected total bill {expected_total} but got {total_bill}"

@pytest.mark.parametrize("tier,consumption,rate", [
    ("Tier 1", 20, 0.57),
    ("Tier 2", 15, 1.03),
    ("Tier 3", 1, 1.40),
])
def test_individual_tiers(exercise_path, tier, consumption, rate):
    """Test each pricing tier individually"""
    if tier == "Tier 1":
        current = 1000 + consumption
        expected_water_cost = consumption * rate
    elif tier == "Tier 2":
        current = 1000 + 20 + consumption  # 20 from tier 1 + consumption from tier 2
        expected_water_cost = (20 * 0.57) + (consumption * rate)
    else:  # Tier 3
        current = 1000 + 35 + consumption  # 35 from tiers 1&2 + consumption from tier 3
        expected_water_cost = (20 * 0.57) + (15 * 1.03) + (consumption * rate)
    
    inputs = f"{current}\n1000\n"
    output = run_exercise(exercise_path, inputs)
    
    actual_consumption, actual_water_cost, _ = extract_results(output)
    
    expected_consumption = current - 1000
    assert actual_consumption == expected_consumption, f"Expected consumption {expected_consumption} but got {actual_consumption}"
    assert abs(actual_water_cost - expected_water_cost) < 0.01, f"Expected water cost {expected_water_cost} but got {actual_water_cost}"