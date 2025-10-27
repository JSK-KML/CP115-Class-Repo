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
        with open('labs/lab13/exercise1/exercise1.py', 'r') as f:
            code = f.read()
        exec(code, {'__name__': '__main__'})
    finally:
        sys.stdin = original_stdin
        sys.stdout = original_stdout

    return output_stream.getvalue().strip().split('\n')

def test_correct_first_attempt():
    """Test correct password on first attempt"""
    result = run_exercise(['python123'])
    assert result[0] == 'True', "Should be logged in successfully"
    assert result[1] == '1', "Should use only 1 attempt"

def test_correct_second_attempt():
    """Test correct password on second attempt"""
    result = run_exercise(['wrong1', 'python123'])
    assert result[0] == 'True', "Should be logged in successfully"
    assert result[1] == '2', "Should use 2 attempts"

def test_correct_third_attempt():
    """Test correct password on third attempt"""
    result = run_exercise(['wrong1', 'wrong2', 'python123'])
    assert result[0] == 'True', "Should be logged in successfully"
    assert result[1] == '3', "Should use 3 attempts"

def test_all_wrong_attempts():
    """Test all wrong attempts"""
    result = run_exercise(['wrong1', 'wrong2', 'wrong3'])
    assert result[0] == 'False', "Should not be logged in"
    assert result[1] == '3', "Should use all 3 attempts"

def test_stops_after_correct():
    """Test that it stops immediately after correct password"""
    result = run_exercise(['python123', 'should_not_read_this'])
    assert result[0] == 'True', "Should be logged in successfully"
    assert result[1] == '1', "Should only use 1 attempt and stop"
