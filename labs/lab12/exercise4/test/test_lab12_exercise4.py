import subprocess
import sys
import os

def run_exercise4(*inputs):
    """Run exercise4.py with given inputs and return output lines."""
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    script_path = os.path.join(script_dir, 'exercise4.py')

    input_data = '\n'.join(str(x) for x in inputs) + '\n'

    result = subprocess.run([sys.executable, script_path],
                          input=input_data, text=True, capture_output=True)

    if result.returncode != 0:
        raise Exception(f"Script failed: {result.stderr}")

    lines = result.stdout.strip().split('\n')
    return int(lines[0]), int(lines[1]), float(lines[2])

def test_all_passing():
    """Test with all passing scores"""
    scores = [60, 75, 85, 100, "end"]
    inputs = scores
    passing_count, failing_count, pass_rate = run_exercise4(*inputs)
    assert passing_count == 4, f"Input: {inputs} | Expected passing_count: 4 | Got: {passing_count}"
    assert failing_count == 0, f"Input: {inputs} | Expected failing_count: 0 | Got: {failing_count}"
    assert pass_rate == 100.00, f"Input: {inputs} | Expected pass_rate: 100.00 | Got: {pass_rate}"

def test_all_failing():
    """Test with all failing scores"""
    scores = [0, 25, 40, 59, "end"]
    inputs = scores
    passing_count, failing_count, pass_rate = run_exercise4(*inputs)
    assert passing_count == 0, f"Input: {inputs} | Expected passing_count: 0 | Got: {passing_count}"
    assert failing_count == 4, f"Input: {inputs} | Expected failing_count: 4 | Got: {failing_count}"
    assert pass_rate == 0.00, f"Input: {inputs} | Expected pass_rate: 0.00 | Got: {pass_rate}"

def test_mixed_scores():
    """Test with mixed passing and failing scores"""
    scores = [45, 70, 55, 80, 90, 30, "end"]
    inputs = scores
    passing_count, failing_count, pass_rate = run_exercise4(*inputs)
    assert passing_count == 3, f"Input: {inputs} | Expected passing_count: 3 | Got: {passing_count}"
    assert failing_count == 3, f"Input: {inputs} | Expected failing_count: 3 | Got: {failing_count}"
    assert pass_rate == 50.00, f"Input: {inputs} | Expected pass_rate: 50.00 | Got: {pass_rate}"

def test_boundary_passing():
    """Test boundary score 60 (passing)"""
    scores = [60, "end"]
    inputs = scores
    passing_count, failing_count, pass_rate = run_exercise4(*inputs)
    assert passing_count == 1, f"Input: {inputs} | Expected passing_count: 1 | Got: {passing_count}"
    assert failing_count == 0, f"Input: {inputs} | Expected failing_count: 0 | Got: {failing_count}"
    assert pass_rate == 100.00, f"Input: {inputs} | Expected pass_rate: 100.00 | Got: {pass_rate}"

def test_boundary_failing():
    """Test boundary score 59 (failing)"""
    scores = [59, "end"]
    inputs = scores
    passing_count, failing_count, pass_rate = run_exercise4(*inputs)
    assert passing_count == 0, f"Input: {inputs} | Expected passing_count: 0 | Got: {passing_count}"
    assert failing_count == 1, f"Input: {inputs} | Expected failing_count: 1 | Got: {failing_count}"
    assert pass_rate == 0.00, f"Input: {inputs} | Expected pass_rate: 0.00 | Got: {pass_rate}"

def test_end_immediately():
    """Test with 'end' immediately"""
    scores = ["end"]
    inputs = scores
    passing_count, failing_count, pass_rate = run_exercise4(*inputs)
    assert passing_count == 0, f"Input: {inputs} | Expected passing_count: 0 | Got: {passing_count}"
    assert failing_count == 0, f"Input: {inputs} | Expected failing_count: 0 | Got: {failing_count}"
    assert pass_rate == 0.00, f"Input: {inputs} | Expected pass_rate: 0.00 | Got: {pass_rate}"

def test_mostly_passing():
    """Test with mostly passing scores"""
    scores = [70, 80, 90, 100, 50, "end"]
    inputs = scores
    passing_count, failing_count, pass_rate = run_exercise4(*inputs)
    assert passing_count == 4, f"Input: {inputs} | Expected passing_count: 4 | Got: {passing_count}"
    assert failing_count == 1, f"Input: {inputs} | Expected failing_count: 1 | Got: {failing_count}"
    assert pass_rate == 80.00, f"Input: {inputs} | Expected pass_rate: 80.00 | Got: {pass_rate}"

def test_mostly_failing():
    """Test with mostly failing scores"""
    scores = [30, 40, 50, 55, 75, "end"]
    inputs = scores
    passing_count, failing_count, pass_rate = run_exercise4(*inputs)
    assert passing_count == 1, f"Input: {inputs} | Expected passing_count: 1 | Got: {passing_count}"
    assert failing_count == 4, f"Input: {inputs} | Expected failing_count: 4 | Got: {failing_count}"
    assert pass_rate == 20.00, f"Input: {inputs} | Expected pass_rate: 20.00 | Got: {pass_rate}"

def test_decimal_pass_rate():
    """Test with decimal pass rate"""
    scores = [70, 80, 50, "end"]
    inputs = scores
    passing_count, failing_count, pass_rate = run_exercise4(*inputs)
    assert passing_count == 2, f"Input: {inputs} | Expected passing_count: 2 | Got: {passing_count}"
    assert failing_count == 1, f"Input: {inputs} | Expected failing_count: 1 | Got: {failing_count}"
    assert pass_rate == 66.67, f"Input: {inputs} | Expected pass_rate: 66.67 | Got: {pass_rate}"

def test_many_scores():
    """Test with many scores"""
    scores = [0, 20, 40, 60, 80, 100, 55, 65, 75, 85, "end"]
    inputs = scores
    passing_count, failing_count, pass_rate = run_exercise4(*inputs)
    assert passing_count == 6, f"Input: {inputs} | Expected passing_count: 6 | Got: {passing_count}"
    assert failing_count == 4, f"Input: {inputs} | Expected failing_count: 4 | Got: {failing_count}"
    assert pass_rate == 60.00, f"Input: {inputs} | Expected pass_rate: 60.00 | Got: {pass_rate}"
