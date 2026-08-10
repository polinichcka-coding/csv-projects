from tracker.analysis import (
    total_income,
    total_expenses,
    balance,
    expenses_by_category,
    biggest_expense,
    average_expense
)

def generate_report(transactions):
    income=total_income(transactions)
    expenses=total_expenses(transactions)
    bal=balance(transactions)
    categories=expenses_by_category(transactions)
    biggest=biggest_expense(transactions)
    average=average_expense(transactions)

    report=f"""FINANCE REPORT
    Total income:{income:.2f}
    Total expenses:{expenses:.2f}
    Balance:{bal:.2f}
    Average expense:{average:.2f}

    Expenses by category:
    """
    for category,amount in categories.items():
        report+=f"{category}:{amount:.2f}\n"

    report+=f"\nBiggestexpense:{biggest}\n"

    return report

def save_report(report, filename):
    with open(filename, "w") as file:
        file.write(report)