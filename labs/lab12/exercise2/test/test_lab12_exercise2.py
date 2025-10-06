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
    return int(lines[0]), float(lines[1]), float(lines[2])

def test_single_score():
    """Test with single valid score"""
    scores = [85, -1]
    inputs = scores
    score_count, total_score, average_score = run_exercise2(*inputs)
    assert score_count == 1, f"Input: {inputs} | Expected score_count: 1 | Got: {score_count}"
    assert total_score == 85.0, f"Input: {inputs} | Expected total_score: 85.0 | Got: {total_score}"
    assert average_score == 85.00, f"Input: {inputs} | Expected average_score: 85.00 | Got: {average_score}"

def test_multiple_scores():
    """Test with multiple valid scores"""
    scores = [70, 85, 90, 95, 101]
    inputs = scores
    score_count, total_score, average_score = run_exercise2(*inputs)
    assert score_count == 4, f"Input: {inputs} | Expected score_count: 4 | Got: {score_count}"
    assert total_score == 340.0, f"Input: {inputs} | Expected total_score: 340.0 | Got: {total_score}"
    assert average_score == 85.00, f"Input: {inputs} | Expected average_score: 85.00 | Got: {average_score}"

def test_sentinel_immediately():
    """Test with sentinel value immediately"""
    scores = [-5]
    inputs = scores
    score_count, total_score, average_score = run_exercise2(*inputs)
    assert score_count == 0, f"Input: {inputs} | Expected score_count: 0 | Got: {score_count}"
    assert total_score == 0.0, f"Input: {inputs} | Expected total_score: 0.0 | Got: {total_score}"
    assert average_score == 0.00, f"Input: {inputs} | Expected average_score: 0.00 | Got: {average_score}"

def test_boundary_scores():
    """Test with boundary scores 0 and 100"""
    scores = [0, 100, 50, 101]
    inputs = scores
    score_count, total_score, average_score = run_exercise2(*inputs)
    assert score_count == 3, f"Input: {inputs} | Expected score_count: 3 | Got: {score_count}"
    assert total_score == 150.0, f"Input: {inputs} | Expected total_score: 150.0 | Got: {total_score}"
    assert average_score == 50.00, f"Input: {inputs} | Expected average_score: 50.00 | Got: {average_score}"

def test_all_same_scores():
    """Test with all same scores"""
    scores = [75, 75, 75, 75, -1]
    inputs = scores
    score_count, total_score, average_score = run_exercise2(*inputs)
    assert score_count == 4, f"Input: {inputs} | Expected score_count: 4 | Got: {score_count}"
    assert total_score == 300.0, f"Input: {inputs} | Expected total_score: 300.0 | Got: {total_score}"
    assert average_score == 75.00, f"Input: {inputs} | Expected average_score: 75.00 | Got: {average_score}"

def test_decimal_scores():
    """Test with decimal scores"""
    scores = [85.5, 92.3, 78.7, 101]
    inputs = scores
    score_count, total_score, average_score = run_exercise2(*inputs)
    assert score_count == 3, f"Input: {inputs} | Expected score_count: 3 | Got: {score_count}"
    assert total_score == 256.5, f"Input: {inputs} | Expected total_score: 256.5 | Got: {total_score}"
    assert average_score == 85.50, f"Input: {inputs} | Expected average_score: 85.50 | Got: {average_score}"

def test_low_scores():
    """Test with low scores"""
    scores = [10, 20, 15, 25, -1]
    inputs = scores
    score_count, total_score, average_score = run_exercise2(*inputs)
    assert score_count == 4, f"Input: {inputs} | Expected score_count: 4 | Got: {score_count}"
    assert total_score == 70.0, f"Input: {inputs} | Expected total_score: 70.0 | Got: {total_score}"
    assert average_score == 17.50, f"Input: {inputs} | Expected average_score: 17.50 | Got: {average_score}"

def test_high_scores():
    """Test with high scores"""
    scores = [95, 98, 100, 99, 200]
    inputs = scores
    score_count, total_score, average_score = run_exercise2(*inputs)
    assert score_count == 4, f"Input: {inputs} | Expected score_count: 4 | Got: {score_count}"
    assert total_score == 392.0, f"Input: {inputs} | Expected total_score: 392.0 | Got: {total_score}"
    assert average_score == 98.00, f"Input: {inputs} | Expected average_score: 98.00 | Got: {average_score}"

def test_mixed_range_scores():
    """Test with scores across the range"""
    scores = [0, 50, 100, -1]
    inputs = scores
    score_count, total_score, average_score = run_exercise2(*inputs)
    assert score_count == 3, f"Input: {inputs} | Expected score_count: 3 | Got: {score_count}"
    assert total_score == 150.0, f"Input: {inputs} | Expected total_score: 150.0 | Got: {total_score}"
    assert average_score == 50.00, f"Input: {inputs} | Expected average_score: 50.00 | Got: {average_score}"

def test_negative_sentinel():
    """Test with negative sentinel after valid scores"""
    scores = [60, 70, 80, -50]
    inputs = scores
    score_count, total_score, average_score = run_exercise2(*inputs)
    assert score_count == 3, f"Input: {inputs} | Expected score_count: 3 | Got: {score_count}"
    assert total_score == 210.0, f"Input: {inputs} | Expected total_score: 210.0 | Got: {total_score}"
    assert average_score == 70.00, f"Input: {inputs} | Expected average_score: 70.00 | Got: {average_score}"
