import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tracker import expenses_by_category
from tracker import total_expenses

def test_expenses_by_category():
    expenses=[
        {
            "category":"food",
            "amount":10
        },
        {
            "category":"food",
            "amount":5
        }
    ]
    result=expenses_by_category(expenses)
    assert result["food"]==15

def test_total_expenses():
    expenses=[
        {
            "category": "food",
            "amount": 100
        }, 
        {
            "category": "transport",
            "amount":12
        }
    ]
    result=total_expenses(expenses)
    assert result==112