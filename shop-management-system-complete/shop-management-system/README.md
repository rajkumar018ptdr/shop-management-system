# Shop Inventory & Billing System

A command-line Python application for a small retail/electronics/hardware shop.

## Main Features
- Inventory: add, view, search, edit, delete, stock update, low-stock report
- Billing: cart, quantity validation, stock deduction, cash/online/udhaar, bill history
- Customers: records, khata/pending amount, payment recording
- Warranty: purchase date, warranty period, expiry and search
- Reports: revenue, gross profit, stock and pending khata dashboard
- JSON persistence and input validation

## Technology
Python 3; standard library only; JSON local storage; CLI.

## Run
```bash
python main.py
```

## Test
```bash
python -m unittest discover -s tests -v
```

## Structure
`main.py` coordinates the CLI. `inventory.py`, `billing.py`, `customer.py`, `warranty.py` and `reports.py` contain feature modules. `storage.py` handles JSON persistence and `validators.py` handles input validation.
