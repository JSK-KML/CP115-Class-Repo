import pytest
import subprocess
import sys
import os

@pytest.fixture
def exercise_path():
    """Fixture to get the path to exercise2.py"""
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'exercise2.py')

def run_exercise(exercise_path, inputs):
    """Run exercise2.py with given inputs and return output"""
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
    """Extract employee name, tax rate, and net salary from output"""
    lines = output.strip().split('\n')
    if len(lines) < 3:
        pytest.fail(f"Expected 3 output lines but got {len(lines)}: {lines}")
    
    employee_name = lines[0].strip()
    tax_rate = lines[1].strip()
    net_salary = float(lines[2].strip())
    
    return employee_name, tax_rate, net_salary

@pytest.mark.parametrize("base_salary,overtime_hours,tax_status,expected_tax_rate,expected_net_salary", [
    # Single status tests
    (4000, 0, "Single", "18%", 2902.80),  # 4000 * 0.82 * 0.885 = 2902.80
    (5000, 0, "Single", "22%", 3451.50),  # 5000 * 0.78 * 0.885 = 3451.50
    (3000, 10, "Single", "18%", 2431.09), # (3000 + 350) * 0.82 * 0.885 = 2431.09
    
    # Married status tests  
    (5000, 0, "Married", "15%", 3761.25), # 5000 * 0.85 * 0.885 = 3761.25
    (6000, 0, "Married", "20%", 4248.00), # 6000 * 0.80 * 0.885 = 4248.00
    (4000, 20, "Married", "15%", 3535.57), # (4000 + 700) = 4700 * 0.85 * 0.885 = 3535.575
    
    # Head status tests
    (5000, 0, "Head", "19%", 3584.25),   # 5000 * 0.81 * 0.885 = 3584.25
    (5500, 0, "Head", "25%", 3650.62),   # 5500 * 0.75 * 0.885 = 3650.625 (rounded to 3650.62)
    (3000, 15, "Head", "19%", 2526.90),  # (3000 + 525) * 0.81 * 0.885 = 2526.90
])
def test_tax_calculations(exercise_path, base_salary, overtime_hours, tax_status, expected_tax_rate, expected_net_salary):
    """Test various tax calculation scenarios"""
    inputs = f"Test Employee\n{base_salary}\n{overtime_hours}\n{tax_status}\n"
    output = run_exercise(exercise_path, inputs)
    
    employee_name, actual_tax_rate, actual_net_salary = extract_results(output)
    
    assert employee_name == "Test Employee", f"Expected 'Test Employee' but got '{employee_name}'"
    assert actual_tax_rate == expected_tax_rate, f"Expected tax rate '{expected_tax_rate}' but got '{actual_tax_rate}'"
    assert abs(actual_net_salary - expected_net_salary) < 0.01, f"Expected net salary {expected_net_salary} but got {actual_net_salary}"

@pytest.mark.parametrize("base_salary,tax_status,expected_tax_rate", [
    # Boundary tests - exactly at threshold
    (5000, "Single", "22%"),   # Exactly at 5000 threshold
    (4999, "Single", "18%"),   # Just below 5000 threshold  
    (6000, "Married", "20%"),  # Exactly at 6000 threshold
    (5999, "Married", "15%"),  # Just below 6000 threshold
    (5500, "Head", "25%"),     # Exactly at 5500 threshold
    (5499, "Head", "19%"),     # Just below 5500 threshold
])
def test_tax_rate_boundaries(exercise_path, base_salary, tax_status, expected_tax_rate):
    """Test tax rate boundary conditions"""
    inputs = f"Test Employee\n{base_salary}\n0\n{tax_status}\n"
    output = run_exercise(exercise_path, inputs)
    
    _, actual_tax_rate, _ = extract_results(output)
    assert actual_tax_rate == expected_tax_rate, f"Expected tax rate '{expected_tax_rate}' but got '{actual_tax_rate}'"

def test_overtime_calculation(exercise_path):
    """Test overtime pay calculation (RM35 per hour)"""
    inputs = "Test Employee\n3000\n10\nSingle\n"  # 10 hours overtime = RM350
    output = run_exercise(exercise_path, inputs)
    
    # Total income should be 3000 + (10 * 35) = 3350
    # Single, >= 5000: No, so 18% tax
    # Net: 3350 * 0.82 * 0.885 = 2430.87
    _, tax_rate, net_salary = extract_results(output)
    
    assert tax_rate == "18%", f"Expected '18%' tax rate but got '{tax_rate}'"
    # Allow small floating point differences
    expected_net = 2430.87
    assert abs(net_salary - expected_net) < 1.0, f"Expected net salary around {expected_net} but got {net_salary}"

def test_deductions_applied(exercise_path):
    """Test that EPF (11%) and SOCSO (0.5%) deductions are applied"""
    inputs = "Test Employee\n1000\n0\nSingle\n"  # Low salary, 18% tax
    output = run_exercise(exercise_path, inputs)
    
    # Expected calculation:
    # Total income: 1000
    # After tax (18%): 1000 * 0.82 = 820
    # After EPF (11%) and SOCSO (0.5%): 820 * 0.885 = 725.70
    _, _, net_salary = extract_results(output)
    
    expected_net = 725.70
    assert abs(net_salary - expected_net) < 0.01, f"Expected net salary {expected_net} but got {net_salary}"