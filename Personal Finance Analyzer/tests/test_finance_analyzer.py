from tracker.io import read_transactions
from tracker.analysis import (
    total_income,
    total_expenses,
    balance,
    biggest_expense,
    expenses_by_category,
    filter_by_category,
    search_transactions,
)


transactions = read_transactions("data/text.csv")


def test_total_income():
    assert total_income(transactions) == 1500.0


def test_total_expenses():
    assert total_expenses(transactions) == 192.5


def test_balance():
    assert balance(transactions) == 1307.5


def test_biggest_expense():
    result = biggest_expense(transactions)

    assert result["amount"] == 100.0
    assert result["category"] == "shopping"


def test_expenses_by_category():
    assert expenses_by_category(transactions) == {
        "food": 12.5,
        "shopping": 180.0,
    }


def test_filter_by_category():
    result = filter_by_category(transactions, "shopping")

    assert len(result) == 2


def test_search_transactions():
    result = search_transactions(transactions, "clothes")

    assert len(result) == 2


test_total_income()
test_total_expenses()
test_balance()
test_biggest_expense()
test_expenses_by_category()
test_filter_by_category()
test_search_transactions()

print("All tests passed!")
