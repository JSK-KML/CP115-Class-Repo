import pytest
import subprocess
import sys
import os

@pytest.fixture
def exercise_path():
    """Fixture to get the path to exercise5.py"""
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'exercise5.py')

def run_exercise(exercise_path, inputs):
    """Run exercise5.py with given inputs and return output"""
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

def extract_final_bill(output):
    """Extract final bill from output"""
    lines = output.strip().split('\n')
    if len(lines) < 1:
        pytest.fail(f"Expected at least 1 output line but got {len(lines)}: {lines}")
    
    return float(lines[-1].strip())

@pytest.mark.parametrize("main_course,drink,dessert,age,expected_bill", [
    ("Chicken", "Soft Drink", "Ice Cream", 25, 17.60),  # Adult, no discount
    ("Beef", "Coffee", "Cake", 65, 18.70),  # Senior discount
    ("Fish", "Soft Drink", "Ice Cream", 16, 16.83),  # Student discount
])
def test_restaurant_billing(exercise_path, main_course, drink, dessert, age, expected_bill):
    """Test restaurant billing calculations with various scenarios"""
    inputs = f"{main_course}\n{drink}\n{dessert}\n{age}\n"
    output = run_exercise(exercise_path, inputs)
    
    final_bill = extract_final_bill(output)
    
    assert abs(final_bill - expected_bill) < 0.01, f"\nInput: {main_course}, {drink}, {dessert}, Age={age}\nExpected: {expected_bill}, Got: {final_bill}"

def test_service_charge_calculation(exercise_path):
    """Test that 10% service charge is applied correctly"""
    inputs = "Chicken\nSoft Drink\nIce Cream\n25\n"  # Adult, no discount
    output = run_exercise(exercise_path, inputs)
    
    final_bill = extract_final_bill(output)
    base_cost = 10 + 2 + 4  # 16
    expected_with_service = base_cost * 1.1  # 17.60
    
    assert abs(final_bill - expected_with_service) < 0.01, f"\nInput: Chicken, Soft Drink, Ice Cream, Age=25\nExpected: {expected_with_service}, Got: {final_bill}"

def test_age_discounts(exercise_path):
    """Test age-based discounts"""
    # Senior discount
    inputs = "Chicken\nSoft Drink\nIce Cream\n65\n"
    output = run_exercise(exercise_path, inputs)
    final_bill = extract_final_bill(output)
    expected = (10 + 2 + 4) * 1.1 * 0.85  # 15% off
    assert abs(final_bill - expected) < 0.01, f"\nInput: Chicken, Soft Drink, Ice Cream, Age=65\nExpected: {expected}, Got: {final_bill}"
    
    # Student discount
    inputs = "Chicken\nSoft Drink\nIce Cream\n17\n"
    output = run_exercise(exercise_path, inputs)
    final_bill = extract_final_bill(output)
    expected = (10 + 2 + 4) * 1.1 * 0.90  # 10% off
    assert abs(final_bill - expected) < 0.01, f"\nInput: Chicken, Soft Drink, Ice Cream, Age=17\nExpected: {expected}, Got: {final_bill}"