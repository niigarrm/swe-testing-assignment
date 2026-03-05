# Quick-Calc (SWE Testing Assignment)

Quick-Calc is a simple calculator that supports:
- Addition, subtraction, multiplication, division (division by zero handled)
- Clear (C) to reset input/result to 0

The focus of this project is testing quality and version control workflow.

## Project Structure
- `quick_calc/core.py` — core calculation logic (unit tested)
- `quick_calc/app.py` — input/UI simulation layer (integration tested)
- `tests/` — unit + integration tests

## Requirements
- Python 3.10+ recommended

## Run Tests
Install pytest:
```bash
python3 -m pip install pytest
