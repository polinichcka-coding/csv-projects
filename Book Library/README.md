## Book analyzer

# How it works
It shows some statistics about genre, authors, ratings

# Structure

book_analyzer/ 
│ 
├── analyzer.py 
├── README.md 
│ 
├── data/ 
│ └── text.csv 
|── tests/ 
    └── test_analyzer.py

In the first row of the file, there are:
title,author,genre,year,rating

# For testing

pip install pytest
pytest

# For checking

python cli.py
