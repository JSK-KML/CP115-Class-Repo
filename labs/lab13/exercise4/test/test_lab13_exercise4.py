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
        with open('labs/lab13/exercise4/exercise4.py', 'r') as f:
            code = f.read()
        exec(code, {'__name__': '__main__'})
    finally:
        sys.stdin = original_stdin
        sys.stdout = original_stdout

    return output_stream.getvalue().strip().split('\n')

def test_only_positive_numbers():
    """Test with only positive numbers"""
    result = run_exercise(['5', '10', '3.5', '0'])
    assert result[0] == '3', "Should count 3 positive numbers"
    assert result[1] == '18.50', "Sum should be 18.50"

def test_skip_negative_numbers():
    """Test that negative numbers are skipped"""
    result = run_exercise(['5', '-3', '10', '-7', '2', '0'])
    assert result[0] == '3', "Should count only 3 positive numbers"
    assert result[1] == '17.00', "Sum should be 17.00"

def test_mixed_positive_negative():
    """Test with mixed positive and negative numbers"""
    result = run_exercise(['10', '-5', '20', '-10', '30', '0'])
    assert result[0] == '3', "Should count 3 positive numbers"
    assert result[1] == '60.00', "Sum should be 60.00"

def test_zero_stops_immediately():
    """Test that 0 stops the loop immediately"""
    result = run_exercise(['0'])
    assert result[0] == '0', "Should count 0 positive numbers"
    assert result[1] == '0.00', "Sum should be 0.00"

def test_only_negative_then_zero():
    """Test with only negative numbers before zero"""
    result = run_exercise(['-5', '-10', '-3', '0'])
    assert result[0] == '0', "Should count 0 positive numbers"
    assert result[1] == '0.00', "Sum should be 0.00"

def test_decimal_positive_numbers():
    """Test with decimal positive numbers"""
    result = run_exercise(['1.5', '2.5', '3.5', '0'])
    assert result[0] == '3', "Should count 3 positive numbers"
    assert result[1] == '7.50', "Sum should be 7.50"
