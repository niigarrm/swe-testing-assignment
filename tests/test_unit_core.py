import pytest
from quick_calc.core import add, subtract, multiply, divide, CalculatorState, clear

def test_addition_basic():
    assert add(5, 3) == 8

def test_subtraction_basic():
    assert subtract(10, 4) == 6

def test_multiplication_basic():
    assert multiply(6, 7) == 42

def test_division_basic():
    assert divide(8, 2) == 4

def test_division_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_negative_numbers():
    assert add(-5, -3) == -8
    assert subtract(-5, 3) == -8

def test_decimal_numbers():
    assert add(0.1, 0.2) == pytest.approx(0.3)
    assert divide(1, 4) == 0.25

def test_very_large_numbers():
    assert multiply(10**12, 10**6) == 10**18

def test_clear_resets_state():
    s = CalculatorState(current="123", result=999, pending_op="+", reset_next=True)
    clear(s)
    assert s.current == "0"
    assert s.result == 0.0
    assert s.pending_op is None
    assert s.reset_next is False
