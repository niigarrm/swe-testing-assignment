
---

## COMMIT 2 — `feat: implement core calculator operations and state`

### `quick_calc/core.py`
```python
from dataclasses import dataclass

@dataclass
class CalculatorState:
    current: str = "0"
    result: float = 0.0
    pending_op: str | None = None
    reset_next: bool = False


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def clear(state: CalculatorState) -> CalculatorState:
    state.current = "0"
    state.result = 0.0
    state.pending_op = None
    state.reset_next = False
    return state


def to_number(s: str) -> float:
    return float(s)
