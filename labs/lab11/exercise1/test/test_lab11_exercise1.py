import subprocess
import sys
import os

def run_exercise1(*inputs):
    """Run exercise1.py with given inputs and return output lines."""
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    script_path = os.path.join(script_dir, 'exercise1.py')

    input_data = '\n'.join(str(x) for x in inputs) + '\n'

    result = subprocess.run([sys.executable, script_path],
                          input=input_data, text=True, capture_output=True)

    if result.returncode != 0:
        raise Exception(f"Script failed: {result.stderr}")

    lines = result.stdout.strip().split('\n')
    return float(lines[0]), int(lines[1])

def test_basic_scores_no_bonus():
    """Test basic scores without bonus (all scores <= 100)"""
    num_rounds = 3
    scores = [50, 75, 100]
    inputs = [num_rounds] + scores
    final_score, rounds_processed = run_exercise1(*inputs)
    expected_total = 225.0  # 50 + 75 + 100
    assert final_score == expected_total, f"Expected final_score: {expected_total} | Got: {final_score}"
    assert rounds_processed == 3, f"Expected rounds_processed: 3 | Got: {rounds_processed}"

def test_single_score_with_bonus():
    """Test single score above 100 with 20% bonus"""
    num_rounds = 1
    scores = [120]
    inputs = [num_rounds] + scores
    final_score, rounds_processed = run_exercise1(*inputs)
    expected_total = 144.0  # 120 + (120 * 0.2) = 120 + 24
    assert final_score == expected_total, f"Expected final_score: {expected_total} | Got: {final_score}"
    assert rounds_processed == 1, f"Expected rounds_processed: 1 | Got: {rounds_processed}"

def test_mixed_scores_with_bonus():
    """Test mix of scores with and without bonus"""
    num_rounds = 4
    scores = [80, 120, 90, 150]
    inputs = [num_rounds] + scores
    final_score, rounds_processed = run_exercise1(*inputs)
    # 80 + (120 + 24) + 90 + (150 + 30) = 80 + 144 + 90 + 180 = 494
    expected_total = 494.0
    assert final_score == expected_total, f"Expected final_score: {expected_total} | Got: {final_score}"
    assert rounds_processed == 4, f"Expected rounds_processed: 4 | Got: {rounds_processed}"

def test_all_bonus_scores():
    """Test all scores above 100 with bonus"""
    num_rounds = 3
    scores = [110, 125, 200]
    inputs = [num_rounds] + scores
    final_score, rounds_processed = run_exercise1(*inputs)
    # (110 + 22) + (125 + 25) + (200 + 40) = 132 + 150 + 240 = 522
    expected_total = 522.0
    assert final_score == expected_total, f"Expected final_score: {expected_total} | Got: {final_score}"
    assert rounds_processed == 3, f"Expected rounds_processed: 3 | Got: {rounds_processed}"

def test_zero_rounds():
    """Test with zero rounds"""
    num_rounds = 0
    inputs = [num_rounds]
    final_score, rounds_processed = run_exercise1(*inputs)
    expected_total = 0.0
    assert final_score == expected_total, f"Expected final_score: {expected_total} | Got: {final_score}"
    assert rounds_processed == 0, f"Expected rounds_processed: 0 | Got: {rounds_processed}"

def test_large_bonus_score():
    """Test very large score with bonus"""
    num_rounds = 1
    scores = [500]
    inputs = [num_rounds] + scores
    final_score, rounds_processed = run_exercise1(*inputs)
    expected_total = 600.0  # 500 + (500 * 0.2) = 500 + 100
    assert final_score == expected_total, f"Expected final_score: {expected_total} | Got: {final_score}"
    assert rounds_processed == 1, f"Expected rounds_processed: 1 | Got: {rounds_processed}"

def test_edge_case_101():
    """Test score just above 100 threshold"""
    num_rounds = 1
    scores = [101]
    inputs = [num_rounds] + scores
    final_score, rounds_processed = run_exercise1(*inputs)
    expected_total = 121.2  # 101 + (101 * 0.2) = 101 + 20.2
    assert final_score == expected_total, f"Expected final_score: {expected_total} | Got: {final_score}"
    assert rounds_processed == 1, f"Expected rounds_processed: 1 | Got: {rounds_processed}"

def test_many_rounds():
    """Test with many rounds"""
    num_rounds = 5
    scores = [25, 50, 75, 100, 125]
    inputs = [num_rounds] + scores
    final_score, rounds_processed = run_exercise1(*inputs)
    # 25 + 50 + 75 + 100 + (125 + 25) = 25 + 50 + 75 + 100 + 150 = 400
    expected_total = 400.0
    assert final_score == expected_total, f"Expected final_score: {expected_total} | Got: {final_score}"
    assert rounds_processed == 5, f"Expected rounds_processed: 5 | Got: {rounds_processed}"

def test_alternating_bonus():
    """Test alternating bonus and non-bonus scores"""
    num_rounds = 6
    scores = [50, 110, 75, 130, 90, 115]
    inputs = [num_rounds] + scores
    final_score, rounds_processed = run_exercise1(*inputs)
    # 50 + (110 + 22) + 75 + (130 + 26) + 90 + (115 + 23) = 50 + 132 + 75 + 156 + 90 + 138 = 641
    expected_total = 641.0
    assert final_score == expected_total, f"Expected final_score: {expected_total} | Got: {final_score}"
    assert rounds_processed == 6, f"Expected rounds_processed: 6 | Got: {rounds_processed}"

def test_decimal_bonus_calculation():
    """Test bonus calculation with decimal result"""
    num_rounds = 2
    scores = [105, 115]
    inputs = [num_rounds] + scores
    final_score, rounds_processed = run_exercise1(*inputs)
    # (105 + 21) + (115 + 23) = 126 + 138 = 264
    expected_total = 264.0
    assert final_score == expected_total, f"Expected final_score: {expected_total} | Got: {final_score}"
    assert rounds_processed == 2, f"Expected rounds_processed: 2 | Got: {rounds_processed}"