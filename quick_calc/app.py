from quick_calc.core import (
    CalculatorState, add, subtract, multiply, divide, clear, to_number
)

OPS = {"+": add, "-": subtract, "*": multiply, "/": divide}

class QuickCalcApp:
    """
    Minimal input/UI layer that simulates calculator button presses.
    Supports keys: digits, '.', '+', '-', '*', '/', '=', 'C'
    """
    def __init__(self):
        self.state = CalculatorState()

    def display(self) -> str:
        try:
            val = float(self.state.current)
            return str(int(val)) if val.is_integer() else str(val)
        except ValueError:
            return self.state.current

    def press(self, key: str) -> str:
        if key == "C":
            clear(self.state)
            return self.display()

        if key.isdigit() or key == ".":
            return self._press_digit_or_dot(key)

        if key in OPS:
            return self._press_operator(key)

        if key == "=":
            return self._press_equals()

        raise ValueError(f"Unknown key: {key}")

    def _press_digit_or_dot(self, key: str) -> str:
        if self.state.reset_next:
            self.state.current = "0"
            self.state.reset_next = False

        if key == "." and "." in self.state.current:
            return self.display()

        if self.state.current == "0" and key != ".":
            self.state.current = key
        else:
            self.state.current += key
        return self.display()

    def _press_operator(self, op_key: str) -> str:
        if self.state.pending_op is None:
            self.state.result = to_number(self.state.current)
        else:
            self._apply_pending()

        self.state.pending_op = op_key
        self.state.current = "0"
        return self.display()

    def _press_equals(self) -> str:
        if self.state.pending_op is not None:
            self._apply_pending()
            self.state.pending_op = None
            self.state.current = str(self.state.result)
            self.state.reset_next = True
        return self.display()

    def _apply_pending(self):
        op = OPS[self.state.pending_op]
        a = self.state.result
        b = to_number(self.state.current)
        self.state.result = op(a, b)
