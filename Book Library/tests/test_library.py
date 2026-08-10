import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from library import (
    count_books,
    books_by_genre,
    books_by_author,
    highest_rate,
    average_rating,
    filter_by_genre,
    filter_by_rating,
    books_after_year
)

def test_count_books():
    books=[
        {"title": "A"},
        {"title": "B"},
        {"title": "C"}
    ]
    result=count_books(books)
    assert result==3

def test_average_rating():
    books=[
        {"rating": 4.8},
        {"rating": 2.0},
        {"rating": 4.4}
    ]
    result=average_rating(books)
    assert round(result, 2)==3.73