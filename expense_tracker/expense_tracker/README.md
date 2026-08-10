# Expense Tracker

## Description

This project reads CSV file and calculate expenses.
The project demonstrates working with:
    files, lists, dictionaries, loops, functions

# Features

    Read file from CSV format
    Calculate total expenses
    Group expenses by category
    Find the biggest expense
    Calculate average expense
    Find the most expensive category
    Filter expenses above a chosen amount

# Project structure

expense_tracker/ │
├── tracker.py 
├── cli.py 
├── sample_data/ 
   │ └── expenses.csv 
├── tests/ 
   │ └── test_tracker.py 
└── README.md

# CSV format 
Example:
date,category,amount
2025-01-01,food,12.5
2025-01-02,transport,5
2025-01-03,food,20
2025-01-04,books,15
2025-01-05,coffee,3

# How to run
Run the CLI:
python cli.py

Run the tests:
pytest

# Author
Created as learning project to practice Python programming
