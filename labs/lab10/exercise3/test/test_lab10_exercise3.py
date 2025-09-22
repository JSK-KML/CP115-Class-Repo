import subprocess
import sys
import os

def run_exercise3(monthly_income, credit_score, loan_amount):
    """Run exercise3.py with given inputs and return output lines."""
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    script_path = os.path.join(script_dir, 'exercise3.py')

    input_data = f"{monthly_income}\n{credit_score}\n{loan_amount}\n"

    result = subprocess.run([sys.executable, script_path],
                          input=input_data, text=True, capture_output=True)

    if result.returncode != 0:
        raise Exception(f"Script failed: {result.stderr}")

    lines = result.stdout.strip().split('\n')
    # Parse outputs - interest_rate as float, others as int/string
    interest_rate = float(lines[0])
    max_loan_amount = int(lines[1])
    approval_status = lines[2]
    return interest_rate, max_loan_amount, approval_status

def test_excellent_credit_approved():
    """High income, excellent credit, reasonable loan amount"""
    interest_rate, max_loan_amount, approval_status = run_exercise3(5000, 750, 20000)
    assert interest_rate == 3.5
    assert max_loan_amount == 25000
    assert approval_status == "Approved"

def test_good_credit_approved():
    """High income, good credit, within limit"""
    interest_rate, max_loan_amount, approval_status = run_exercise3(6000, 650, 25000)
    assert interest_rate == 5.5
    assert max_loan_amount == 30000
    assert approval_status == "Approved"

def test_poor_credit_rejected():
    """High income, poor credit"""
    interest_rate, max_loan_amount, approval_status = run_exercise3(8000, 550, 30000)
    assert interest_rate == 0.0
    assert max_loan_amount == 40000
    assert approval_status == "Rejected"

def test_low_income_rejected():
    """Low income, excellent credit"""
    interest_rate, max_loan_amount, approval_status = run_exercise3(3000, 750, 10000)
    assert interest_rate == 3.5
    assert max_loan_amount == 15000
    assert approval_status == "Rejected"

def test_loan_too_high_rejected():
    """Good income and credit, but loan amount exceeds 5x income"""
    interest_rate, max_loan_amount, approval_status = run_exercise3(4000, 700, 25000)
    assert interest_rate == 3.5
    assert max_loan_amount == 20000
    assert approval_status == "Rejected"

def test_minimum_requirements_approved():
    """Exactly minimum income and credit, within loan limit"""
    interest_rate, max_loan_amount, approval_status = run_exercise3(4000, 600, 15000)
    assert interest_rate == 5.5
    assert max_loan_amount == 20000
    assert approval_status == "Approved"

def test_boundary_credit_score_600():
    """Credit score exactly 600 (boundary test)"""
    interest_rate, max_loan_amount, approval_status = run_exercise3(5000, 600, 20000)
    assert interest_rate == 5.5
    assert max_loan_amount == 25000
    assert approval_status == "Approved"

def test_boundary_credit_score_700():
    """Credit score exactly 700 (boundary test)"""
    interest_rate, max_loan_amount, approval_status = run_exercise3(5000, 700, 20000)
    assert interest_rate == 3.5
    assert max_loan_amount == 25000
    assert approval_status == "Approved"

def test_high_income_max_loan():
    """High income, requesting maximum allowable loan"""
    interest_rate, max_loan_amount, approval_status = run_exercise3(10000, 750, 50000)
    assert interest_rate == 3.5
    assert max_loan_amount == 50000
    assert approval_status == "Approved"

def test_multiple_rejections():
    """Fails multiple criteria - low income, poor credit, high loan"""
    interest_rate, max_loan_amount, approval_status = run_exercise3(2000, 400, 30000)
    assert interest_rate == 0.0
    assert max_loan_amount == 10000
    assert approval_status == "Rejected"