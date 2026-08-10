from tracker import (
    read_expenses,
    total_expenses,
    expenses_by_category,
    max_purchase,
    average_expense,
    most_expensive_category,
    filter_expenses
)

expenses=read_expenses("sample_data/expenses.csv")

while True:

    print("""
    1. Total expenses
    2. Expenses by category
    3. Biggest purchase
    4. Average expense
    5. Filter expenses
    0. Exit
    """)

    choice = input("Choose: ")

    if choice=="1":
        print(total_expenses(expenses))
    elif choice=="2":
        print(expenses_by_category(expenses))

    elif choice=="3":
        print(max_purchase(expenses))

    elif choice=="4":
        print(average_expense(expenses))

    elif choice=="5":
        limit = float(input("Amount: "))
        print(filter_expenses(expenses, limit))

    elif choice=="0":
        break