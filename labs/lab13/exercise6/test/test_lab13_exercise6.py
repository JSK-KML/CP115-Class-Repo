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
        with open('labs/lab13/exercise6/exercise6.py', 'r') as f:
            code = f.read()
        exec(code, {'__name__': '__main__'})
    finally:
        sys.stdin = original_stdin
        sys.stdout = original_stdout

    return output_stream.getvalue().strip().split('\n')

def test_all_age_groups():
    """Test with all different age groups"""
    result = run_exercise(['10', '15', '25', '70', '-1'])
    # Child ($8) + Teen ($10) + Adult ($15) + Senior ($10) = $43
    assert result[0] == '4', "Should sell 4 tickets"
    assert result[1] == '43', "Total revenue should be $43"

def test_only_children():
    """Test with only children tickets"""
    result = run_exercise(['5', '8', '12', '-1'])
    assert result[0] == '3', "Should sell 3 tickets"
    assert result[1] == '24', "Total revenue should be $24 (3 x $8)"

def test_only_teens():
    """Test with only teen tickets"""
    result = run_exercise(['13', '15', '17', '-1'])
    assert result[0] == '3', "Should sell 3 tickets"
    assert result[1] == '30', "Total revenue should be $30 (3 x $10)"

def test_only_adults():
    """Test with only adult tickets"""
    result = run_exercise(['18', '30', '64', '-1'])
    assert result[0] == '3', "Should sell 3 tickets"
    assert result[1] == '45', "Total revenue should be $45 (3 x $15)"

def test_only_seniors():
    """Test with only senior tickets"""
    result = run_exercise(['65', '75', '80', '-1'])
    assert result[0] == '3', "Should sell 3 tickets"
    assert result[1] == '30', "Total revenue should be $30 (3 x $10)"

def test_boundary_ages():
    """Test boundary ages for each category"""
    result = run_exercise(['0', '12', '13', '17', '18', '64', '65', '-1'])
    # 0-12: Child ($8 x 2), 13-17: Teen ($10 x 2), 18-64: Adult ($15 x 2), 65+: Senior ($10 x 1)
    # Total: $8 + $8 + $10 + $10 + $15 + $15 + $10 = $76
    assert result[0] == '7', "Should sell 7 tickets"
    assert result[1] == '76', "Total revenue should be $76"

def test_no_tickets():
    """Test with no tickets sold"""
    result = run_exercise(['-1'])
    assert result[0] == '0', "Should sell 0 tickets"
    assert result[1] == '0', "Total revenue should be $0"
