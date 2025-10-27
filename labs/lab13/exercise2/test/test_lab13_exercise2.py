import pytest
import sys
from io import StringIO

def run_exercise():
    """Helper function to run exercise and capture output"""
    output_stream = StringIO()
    original_stdout = sys.stdout
    sys.stdout = output_stream

    try:
        with open('labs/lab13/exercise2/exercise2.py', 'r') as f:
            code = f.read()
        exec(code, {'__name__': '__main__'})
    finally:
        sys.stdout = original_stdout

    return output_stream.getvalue().strip()

def test_finds_correct_number():
    """Test that it finds 91 (the first number divisible by both 7 and 13)"""
    result = run_exercise()
    assert result == '91', "Should find 91 as the first number divisible by both 7 and 13"

def test_number_divisible_by_7():
    """Test that found number is divisible by 7"""
    result = int(run_exercise())
    assert result % 7 == 0, f"{result} should be divisible by 7"

def test_number_divisible_by_13():
    """Test that found number is divisible by 13"""
    result = int(run_exercise())
    assert result % 13 == 0, f"{result} should be divisible by 13"

def test_number_in_range():
    """Test that found number is between 1 and 100"""
    result = int(run_exercise())
    assert 1 <= result <= 100, f"{result} should be between 1 and 100"
