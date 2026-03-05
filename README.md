# ExpenseSplit
Python Flask application implementing an O(n log n) heap-based algorithm to minimize group expense settlement transactions.
# Expense Settlement Optimizer

A Flask-based web application that minimizes the number of transactions required to settle group expenses.

## Features
- Multiple expense support
- Exact share splitting
- Heap-based settlement algorithm
- Graph visualization of transactions
- SQLite expense persistence

## Tech Stack
- Python
- Flask
- SQLite
- NetworkX
- Matplotlib

## Algorithm
Uses a priority queue (heap) to match the largest debtor with the largest creditor, reducing settlement complexity to O(n log n).

## How to Run

Install dependencies

pip install -r requirements.txt

Run server

python app.py

Open browser

http://127.0.0.1:5000
