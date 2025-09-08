import pytest
import subprocess
import sys
import os

@pytest.fixture
def exercise_path():
    """Fixture to get the path to exercise3.py"""
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'exercise3.py')

def run_exercise(exercise_path, inputs):
    """Run exercise3.py with given inputs and return output"""
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
    """Extract base price and final price from output"""
    lines = output.strip().split('\n')
    if len(lines) < 2:
        pytest.fail(f"Expected 2 output lines but got {len(lines)}: {lines}")
    
    base_price = float(lines[0].strip())
    final_price = float(lines[1].strip())
    
    return base_price, final_price

@pytest.mark.parametrize("day_type,show_time,customer_type,is_student,expected_base,expected_final", [
    # Weekend pricing (no student discount on weekends)
    ("Weekend", 14, "Adult", "No", 18, 18),      # Weekend Adult daytime
    ("Weekend", 19, "Adult", "No", 18, 21),      # Weekend Adult evening (+3)
    ("Weekend", 14, "Child", "No", 12, 12),      # Weekend Child daytime  
    ("Weekend", 19, "Child", "No", 12, 15),      # Weekend Child evening (+3)
    ("Weekend", 14, "Senior", "No", 15, 15),     # Weekend Senior daytime
    ("Weekend", 19, "Senior", "No", 15, 18),     # Weekend Senior evening (+3)
    ("Weekend", 19, "Adult", "Yes", 18, 21),     # Weekend Student (no discount)
    
    # Weekday pricing without student discount
    ("Weekday", 14, "Adult", "No", 15, 15),      # Weekday Adult daytime
    ("Weekday", 19, "Adult", "No", 15, 18),      # Weekday Adult evening (+3)
    ("Weekday", 14, "Child", "No", 10, 10),      # Weekday Child daytime
    ("Weekday", 19, "Child", "No", 10, 13),      # Weekday Child evening (+3)  
    ("Weekday", 14, "Senior", "No", 12, 12),     # Weekday Senior daytime
    ("Weekday", 19, "Senior", "No", 12, 15),     # Weekday Senior evening (+3)
    
    # Weekday pricing with student discount (10% off final price)
    ("Weekday", 14, "Adult", "Yes", 15, 13.5),   # 15 * 0.9 = 13.5
    ("Weekday", 19, "Adult", "Yes", 15, 16.2),   # (15 + 3) * 0.9 = 16.2
    ("Weekday", 14, "Child", "Yes", 10, 9.0),    # 10 * 0.9 = 9.0
    ("Weekday", 19, "Child", "Yes", 10, 11.7),   # (10 + 3) * 0.9 = 11.7
    ("Weekday", 14, "Senior", "Yes", 12, 10.8),  # 12 * 0.9 = 10.8
    ("Weekday", 19, "Senior", "Yes", 12, 13.5),  # (12 + 3) * 0.9 = 13.5
])
def test_movie_ticket_pricing(exercise_path, day_type, show_time, customer_type, is_student, expected_base, expected_final):
    """Test various movie ticket pricing scenarios"""
    inputs = f"{day_type}\n{show_time}\n{customer_type}\n{is_student}\n"
    output = run_exercise(exercise_path, inputs)
    
    actual_base, actual_final = extract_results(output)
    
    assert abs(actual_base - expected_base) < 0.01, f"Expected base price {expected_base} but got {actual_base}"
    assert abs(actual_final - expected_final) < 0.01, f"Expected final price {expected_final} but got {actual_final}"

@pytest.mark.parametrize("show_time,is_evening", [
    (6, False),    # 6am is not evening
    (18, False),   # 6pm (18:00) is not evening (not after 6pm)
    (19, True),    # 7pm (19:00) is evening (after 6pm)
    (7, False),    # 7am is not evening
    (20, True),    # 8pm is evening
    (12, False),   # Noon is not evening
    (14, False),   # 2pm is not evening
])
def test_evening_time_boundary(exercise_path, show_time, is_evening):
    """Test evening time boundary (after 6pm = +RM3)"""
    inputs = f"Weekday\n{show_time}\nAdult\nNo\n"
    output = run_exercise(exercise_path, inputs)
    
    base_price, final_price = extract_results(output)
    
    assert base_price == 15, f"Base price should always be 15 for weekday adult, got {base_price}"
    
    if is_evening:
        expected_final = 18  # 15 + 3
        assert final_price == expected_final, f"Evening show should cost {expected_final}, got {final_price}"
    else:
        expected_final = 15  # No evening surcharge
        assert final_price == expected_final, f"Daytime show should cost {expected_final}, got {final_price}"

def test_student_discount_only_weekdays(exercise_path):
    """Test that student discount only applies on weekdays"""
    # Weekend student - no discount
    inputs_weekend = "Weekend\n14\nAdult\nYes\n"
    output_weekend = run_exercise(exercise_path, inputs_weekend)
    base_weekend, final_weekend = extract_results(output_weekend)
    
    assert base_weekend == 18, "Weekend adult base price should be 18"
    assert final_weekend == 18, "Weekend student should get no discount"
    
    # Weekday student - 10% discount
    inputs_weekday = "Weekday\n14\nAdult\nYes\n"
    output_weekday = run_exercise(exercise_path, inputs_weekday)
    base_weekday, final_weekday = extract_results(output_weekday)
    
    assert base_weekday == 15, "Weekday adult base price should be 15"
    assert abs(final_weekday - 13.5) < 0.01, f"Weekday student should get 10% discount (13.5), got {final_weekday}"

def test_combined_evening_and_student_discount(exercise_path):
    """Test evening surcharge with student discount (discount applies to final price after evening surcharge)"""
    inputs = "Weekday\n19\nAdult\nYes\n"  # Evening + Student
    output = run_exercise(exercise_path, inputs)
    
    base_price, final_price = extract_results(output)
    
    assert base_price == 15, "Base price should be 15 for weekday adult"
    # Calculation: base (15) + evening surcharge (3) = 18, then student discount: 18 * 0.9 = 16.2
    expected_final = 16.2
    assert abs(final_price - expected_final) < 0.01, f"Expected {expected_final} but got {final_price}"

@pytest.mark.parametrize("customer_type,weekend_price,weekday_price", [
    ("Adult", 18, 15),
    ("Child", 12, 10),
    ("Senior", 15, 12),
])
def test_customer_type_pricing(exercise_path, customer_type, weekend_price, weekday_price):
    """Test base pricing for different customer types"""
    # Weekend pricing
    inputs_weekend = f"Weekend\n14\n{customer_type}\nNo\n"
    output_weekend = run_exercise(exercise_path, inputs_weekend)
    base_weekend, final_weekend = extract_results(output_weekend)
    
    assert base_weekend == weekend_price, f"Weekend {customer_type} base price should be {weekend_price}"
    assert final_weekend == weekend_price, f"Weekend {customer_type} final price should be {weekend_price}"
    
    # Weekday pricing
    inputs_weekday = f"Weekday\n14\n{customer_type}\nNo\n"
    output_weekday = run_exercise(exercise_path, inputs_weekday)
    base_weekday, final_weekday = extract_results(output_weekday)
    
    assert base_weekday == weekday_price, f"Weekday {customer_type} base price should be {weekday_price}"
    assert final_weekday == weekday_price, f"Weekday {customer_type} final price should be {weekday_price}"