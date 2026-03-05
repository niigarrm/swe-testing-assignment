from quick_calc.app import QuickCalcApp
import pytest

def test_full_user_interaction_addition():
    app = QuickCalcApp()
    app.press("5")
    app.press("+")
    app.press("3")
    out = app.press("=")
    assert out == "8"

def test_clear_after_calculation_resets_display():
    app = QuickCalcApp()
    app.press("9")
    app.press("*")
    app.press("9")
    app.press("=")
    assert app.display() == "81"
    out = app.press("C")
    assert out == "0"
    assert app.display() == "0"

def test_division_by_zero_propagates_error_in_flow():
    app = QuickCalcApp()
    app.press("1")
    app.press("/")
    app.press("0")
    with pytest.raises(ZeroDivisionError):
        app.press("=")
