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
    return int(lines[0]), float(lines[1])

def test_single_item():
    """Test with single item"""
    prices = [10.50, -1]
    inputs = prices
    item_count, total_cost = run_exercise1(*inputs)
    assert item_count == 1, f"Input: {inputs} | Expected item_count: 1 | Got: {item_count}"
    assert total_cost == 10.50, f"Input: {inputs} | Expected total_cost: 10.50 | Got: {total_cost}"

def test_multiple_items():
    """Test with multiple items"""
    prices = [15.99, 23.45, 8.00, 12.75, -1]
    inputs = prices
    item_count, total_cost = run_exercise1(*inputs)
    assert item_count == 4, f"Input: {inputs} | Expected item_count: 4 | Got: {item_count}"
    assert total_cost == 60.19, f"Input: {inputs} | Expected total_cost: 60.19 | Got: {total_cost}"

def test_zero_sentinel():
    """Test with negative sentinel immediately"""
    prices = [-5]
    inputs = prices
    item_count, total_cost = run_exercise1(*inputs)
    assert item_count == 0, f"Input: {inputs} | Expected item_count: 0 | Got: {item_count}"
    assert total_cost == 0.00, f"Input: {inputs} | Expected total_cost: 0.00 | Got: {total_cost}"

def test_many_items():
    """Test with many items"""
    prices = [5.00, 10.00, 15.00, 20.00, 25.00, 30.00, -1]
    inputs = prices
    item_count, total_cost = run_exercise1(*inputs)
    assert item_count == 6, f"Input: {inputs} | Expected item_count: 6 | Got: {item_count}"
    assert total_cost == 105.00, f"Input: {inputs} | Expected total_cost: 105.00 | Got: {total_cost}"

def test_decimal_prices():
    """Test with various decimal prices"""
    prices = [9.99, 19.99, 4.50, 7.25, -1]
    inputs = prices
    item_count, total_cost = run_exercise1(*inputs)
    assert item_count == 4, f"Input: {inputs} | Expected item_count: 4 | Got: {item_count}"
    assert total_cost == 41.73, f"Input: {inputs} | Expected total_cost: 41.73 | Got: {total_cost}"

def test_large_price():
    """Test with large price"""
    prices = [999.99, -1]
    inputs = prices
    item_count, total_cost = run_exercise1(*inputs)
    assert item_count == 1, f"Input: {inputs} | Expected item_count: 1 | Got: {item_count}"
    assert total_cost == 999.99, f"Input: {inputs} | Expected total_cost: 999.99 | Got: {total_cost}"

def test_small_prices():
    """Test with small prices"""
    prices = [0.01, 0.99, 1.50, -1]
    inputs = prices
    item_count, total_cost = run_exercise1(*inputs)
    assert item_count == 3, f"Input: {inputs} | Expected item_count: 3 | Got: {item_count}"
    assert total_cost == 2.50, f"Input: {inputs} | Expected total_cost: 2.50 | Got: {total_cost}"

def test_round_numbers():
    """Test with round number prices"""
    prices = [10.00, 20.00, 30.00, -1]
    inputs = prices
    item_count, total_cost = run_exercise1(*inputs)
    assert item_count == 3, f"Input: {inputs} | Expected item_count: 3 | Got: {item_count}"
    assert total_cost == 60.00, f"Input: {inputs} | Expected total_cost: 60.00 | Got: {total_cost}"

def test_mixed_prices():
    """Test with mixed round and decimal prices"""
    prices = [12.00, 15.99, 20.00, 8.45, -1]
    inputs = prices
    item_count, total_cost = run_exercise1(*inputs)
    assert item_count == 4, f"Input: {inputs} | Expected item_count: 4 | Got: {item_count}"
    assert total_cost == 56.44, f"Input: {inputs} | Expected total_cost: 56.44 | Got: {total_cost}"

def test_negative_sentinel_variations():
    """Test with different negative sentinels"""
    prices = [5.00, 10.00, -100]
    inputs = prices
    item_count, total_cost = run_exercise1(*inputs)
    assert item_count == 2, f"Input: {inputs} | Expected item_count: 2 | Got: {item_count}"
    assert total_cost == 15.00, f"Input: {inputs} | Expected total_cost: 15.00 | Got: {total_cost}"
