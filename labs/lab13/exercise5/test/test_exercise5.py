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
        with open('labs/lab13/exercise5/exercise5.py', 'r') as f:
            code = f.read()
        exec(code, {'__name__': '__main__'})
    finally:
        sys.stdin = original_stdin
        sys.stdout = original_stdout

    return output_stream.getvalue().strip().split('\n')

def test_all_valid_withdrawals():
    """Test with all valid withdrawals"""
    result = run_exercise(['20', '40', '100', '0'])
    assert result[0] == '3', "Should count 3 valid withdrawals"
    assert result[1] == '160', "Total should be 160"

def test_skip_below_minimum():
    """Test skipping amounts below $20"""
    result = run_exercise(['10', '20', '40', '0'])
    assert result[0] == '2', "Should count only 2 valid withdrawals"
    assert result[1] == '60', "Total should be 60"

def test_skip_above_maximum():
    """Test skipping amounts above $500"""
    result = run_exercise(['600', '100', '200', '0'])
    assert result[0] == '2', "Should count only 2 valid withdrawals"
    assert result[1] == '300', "Total should be 300"

def test_skip_not_multiples_of_20():
    """Test skipping amounts not multiples of 20"""
    result = run_exercise(['25', '20', '35', '40', '60', '0'])
    assert result[0] == '3', "Should count only 3 valid withdrawals (20, 40, 60)"
    assert result[1] == '120', "Total should be 120"

def test_maximum_valid_withdrawal():
    """Test maximum valid withdrawal of $500"""
    result = run_exercise(['500', '100', '0'])
    assert result[0] == '2', "Should count 2 valid withdrawals"
    assert result[1] == '600', "Total should be 600"

def test_only_invalid_withdrawals():
    """Test with only invalid withdrawals"""
    result = run_exercise(['15', '505', '35', '0'])
    assert result[0] == '0', "Should count 0 valid withdrawals"
    assert result[1] == '0', "Total should be 0"

def test_mixed_valid_invalid():
    """Test with mixed valid and invalid amounts"""
    result = run_exercise(['15', '20', '600', '40', '25', '60', '0'])
    assert result[0] == '3', "Should count 3 valid withdrawals"
    assert result[1] == '120', "Total should be 120"
