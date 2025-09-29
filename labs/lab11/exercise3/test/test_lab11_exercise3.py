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
    return int(lines[0]), int(lines[1])

def test_exact_target_single_round():
    """Test reaching target exactly in one round"""
    target_points = 100
    points = [100]
    inputs = [target_points] + points
    total_points, rounds_played = run_exercise3(*inputs)
    assert total_points == 100, f"Expected total_points: 100 | Got: {total_points}"
    assert rounds_played == 1, f"Expected rounds_played: 1 | Got: {rounds_played}"

def test_exceed_target_single_round():
    """Test exceeding target in one round"""
    target_points = 100
    points = [150]
    inputs = [target_points] + points
    total_points, rounds_played = run_exercise3(*inputs)
    assert total_points == 150, f"Expected total_points: 150 | Got: {total_points}"
    assert rounds_played == 1, f"Expected rounds_played: 1 | Got: {rounds_played}"

def test_multiple_rounds_exact():
    """Test reaching target exactly over multiple rounds"""
    target_points = 100
    points = [30, 45, 25]
    inputs = [target_points] + points
    total_points, rounds_played = run_exercise3(*inputs)
    assert total_points == 100, f"Expected total_points: 100 | Got: {total_points}"
    assert rounds_played == 3, f"Expected rounds_played: 3 | Got: {rounds_played}"

def test_multiple_rounds_exceed():
    """Test exceeding target over multiple rounds"""
    target_points = 100
    points = [30, 45, 35]
    inputs = [target_points] + points
    total_points, rounds_played = run_exercise3(*inputs)
    assert total_points == 110, f"Expected total_points: 110 | Got: {total_points}"
    assert rounds_played == 3, f"Expected rounds_played: 3 | Got: {rounds_played}"

def test_many_small_additions():
    """Test many small point additions"""
    target_points = 50
    points = [10, 10, 10, 10, 10]
    inputs = [target_points] + points
    total_points, rounds_played = run_exercise3(*inputs)
    assert total_points == 50, f"Expected total_points: 50 | Got: {total_points}"
    assert rounds_played == 5, f"Expected rounds_played: 5 | Got: {rounds_played}"

def test_low_target():
    """Test with very low target"""
    target_points = 10
    points = [5, 8]
    inputs = [target_points] + points
    total_points, rounds_played = run_exercise3(*inputs)
    assert total_points == 13, f"Expected total_points: 13 | Got: {total_points}"
    assert rounds_played == 2, f"Expected rounds_played: 2 | Got: {rounds_played}"

def test_high_target():
    """Test with high target"""
    target_points = 1000
    points = [200, 300, 250, 300]
    inputs = [target_points] + points
    total_points, rounds_played = run_exercise3(*inputs)
    assert total_points == 1050, f"Expected total_points: 1050 | Got: {total_points}"
    assert rounds_played == 4, f"Expected rounds_played: 4 | Got: {rounds_played}"

def test_zero_points_then_target():
    """Test adding zero points then reaching target"""
    target_points = 25
    points = [0, 0, 25]
    inputs = [target_points] + points
    total_points, rounds_played = run_exercise3(*inputs)
    assert total_points == 25, f"Expected total_points: 25 | Got: {total_points}"
    assert rounds_played == 3, f"Expected rounds_played: 3 | Got: {rounds_played}"

def test_large_numbers():
    """Test with large point values"""
    target_points = 500
    points = [100, 150, 200, 75]
    inputs = [target_points] + points
    total_points, rounds_played = run_exercise3(*inputs)
    assert total_points == 525, f"Expected total_points: 525 | Got: {total_points}"
    assert rounds_played == 4, f"Expected rounds_played: 4 | Got: {rounds_played}"

def test_target_one():
    """Test with target of 1"""
    target_points = 1
    points = [1]
    inputs = [target_points] + points
    total_points, rounds_played = run_exercise3(*inputs)
    assert total_points == 1, f"Expected total_points: 1 | Got: {total_points}"
    assert rounds_played == 1, f"Expected rounds_played: 1 | Got: {rounds_played}"