import subprocess
import sys
import os

def run_exercise2(age, accident_count):
    """Run exercise2.py with given inputs and return output lines."""
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    script_path = os.path.join(script_dir, 'exercise2.py')

    input_data = f"{age}\n{accident_count}\n"

    result = subprocess.run([sys.executable, script_path],
                          input=input_data, text=True, capture_output=True)

    if result.returncode != 0:
        raise Exception(f"Script failed: {result.stderr}")

    lines = result.stdout.strip().split('\n')
    return [int(line) for line in lines]

def test_young_driver_no_accidents():
    """Age 22, 0 accidents - gets good driver discount"""
    base_premium, final_premium, discount_amount = run_exercise2(22, 0)
    assert base_premium == 2400
    assert final_premium == 2160  # 2400 - 240 (10% discount)
    assert discount_amount == 240

def test_young_driver_one_accident():
    """Age 20, 1 accident - penalty but no discount"""
    base_premium, final_premium, discount_amount = run_exercise2(20, 1)
    assert base_premium == 2400
    assert final_premium == 2700  # 2400 + 300 penalty
    assert discount_amount == 0

def test_middle_aged_no_accidents():
    """Age 35, 0 accidents - gets good driver discount"""
    base_premium, final_premium, discount_amount = run_exercise2(35, 0)
    assert base_premium == 1800
    assert final_premium == 1620  # 1800 - 180 (10% discount)
    assert discount_amount == 180

def test_middle_aged_two_accidents():
    """Age 40, 2 accidents - penalty but no discount"""
    base_premium, final_premium, discount_amount = run_exercise2(40, 2)
    assert base_premium == 1800
    assert final_premium == 2100  # 1800 + 300 penalty
    assert discount_amount == 0

def test_senior_no_accidents():
    """Age 65, 0 accidents - gets good driver discount"""
    base_premium, final_premium, discount_amount = run_exercise2(65, 0)
    assert base_premium == 2000
    assert final_premium == 1800  # 2000 - 200 (10% discount)
    assert discount_amount == 200

def test_senior_many_accidents():
    """Age 55, 5 accidents - high penalty, no discount"""
    base_premium, final_premium, discount_amount = run_exercise2(55, 5)
    assert base_premium == 2000
    assert final_premium == 2600  # 2000 + 600 penalty
    assert discount_amount == 0

def test_exact_age_25_no_accidents():
    """Age 25 (boundary), 0 accidents"""
    base_premium, final_premium, discount_amount = run_exercise2(25, 0)
    assert base_premium == 1800
    assert final_premium == 1620  # 1800 - 180 (10% discount)
    assert discount_amount == 180

def test_exact_age_50_three_accidents():
    """Age 50 (boundary), 3 accidents"""
    base_premium, final_premium, discount_amount = run_exercise2(50, 3)
    assert base_premium == 1800
    assert final_premium == 2400  # 1800 + 600 penalty
    assert discount_amount == 0

def test_young_extreme_accidents():
    """Age 18, 10 accidents - maximum penalty"""
    base_premium, final_premium, discount_amount = run_exercise2(18, 10)
    assert base_premium == 2400
    assert final_premium == 3000  # 2400 + 600 penalty
    assert discount_amount == 0

def test_senior_boundary_one_accident():
    """Age 51, 1 accident - senior premium with penalty"""
    base_premium, final_premium, discount_amount = run_exercise2(51, 1)
    assert base_premium == 2000
    assert final_premium == 2300  # 2000 + 300 penalty
    assert discount_amount == 0