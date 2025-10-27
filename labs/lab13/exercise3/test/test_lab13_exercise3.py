import pytest
import sys
from io import StringIO

def run_exercise(input_values):
    """Helper function to run exercise with given inputs and capture output"""
    input_stream = StringIO('\n'.join(input_values))
    output_stream = StringIO()

    original_stdin = sys.stdin
    original_stdout = sys.stdout

    sys.stdin = input_stream
    sys.stdout = output_stream

    try:
        with open('labs/lab13/exercise3/exercise3.py', 'r') as f:
            code = f.read()
        exec(code, {'__name__': '__main__'})
    finally:
        sys.stdin = original_stdin
        sys.stdout = original_stdout

    return output_stream.getvalue().strip().split('\n')

def test_all_valid_grades():
    """Test with all valid grades"""
    result = run_exercise(['85', '90', '78', '-1'])
    assert result[0] == '3', "Should count 3 valid grades"
    assert result[1] == '84.33', "Average should be 84.33"

def test_skip_invalid_high():
    """Test skipping grades over 100"""
    result = run_exercise(['85', '150', '90', '-1'])
    assert result[0] == '2', "Should count only 2 valid grades"
    assert result[1] == '87.50', "Average should be 87.50"

def test_skip_invalid_low():
    """Test skipping grades less than 0 (but not stopping on -1)"""
    result = run_exercise(['85', '-50', '90', '-1'])
    assert result[0] == '2', "Should count only 2 valid grades"
    assert result[1] == '87.50', "Average should be 87.50"

def test_skip_both_invalid():
    """Test skipping both high and low invalid grades"""
    result = run_exercise(['85', '150', '-50', '90', '101', '78', '-1'])
    assert result[0] == '3', "Should count 3 valid grades"
    assert result[1] == '84.33', "Average should be 84.33"

def test_boundary_values():
    """Test boundary values 0 and 100"""
    result = run_exercise(['0', '100', '50', '-1'])
    assert result[0] == '3', "Should count 3 valid grades (0 and 100 are valid)"
    assert result[1] == '50.00', "Average should be 50.00"

def test_only_invalid_grades():
    """Test with only invalid grades before -1"""
    result = run_exercise(['150', '200', '-50', '-1'])
    assert result[0] == '0', "Should count 0 valid grades"
    assert result[1] == '0.00', "Average should be 0.00"
