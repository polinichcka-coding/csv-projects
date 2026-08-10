from tracker.io import read_transactions, save_transactions
from tracker.analysis import (
    total_income,
    total_expenses,
    balance,
    expenses_by_category,
    biggest_expense,
    average_expense,
    filter_by_category,
    filter_by_date,
    search_transactions
)
from tracker.operations import (
    add_transaction,
    delete_transaction
)
from tracker.report import (
    generate_report,
    save_report
)
from datetime import datetime

filename = "data/text.csv"
transactions = read_transactions(filename)

while True:
    print("""
1. Show transactions
2. Total income
3. Total expenses
4. Balance
5. Expenses by category
6. Biggest expense
7. Average expense
8. Filter by category
9. Filter by date
10. Search transactions
11. Add transaction
12. Delete transaction
13. Report
0. Exit
""")

    choice = input("Choose: ")

    if choice == "1":
        print(transactions)

    elif choice == "2":
        print(total_income(transactions))

    elif choice == "3":
        print(total_expenses(transactions))

    elif choice == "4":
        print(balance(transactions))

    elif choice == "5":
        print(expenses_by_category(transactions))

    elif choice == "6":
        print(biggest_expense(transactions))

    elif choice == "7":
        print(average_expense(transactions))

    elif choice == "8":
        s=input("Category: ")
        print(filter_by_category(transactions, s))

    elif choice == "9":
        start = datetime.strptime(input("Start date: "),"%Y-%m-%d").date()
        end = datetime.strptime(input("End date: "),"%Y-%m-%d").date()       
        print(filter_by_date(transactions, start, end))

    elif choice == "10":
        w=input("word: ")
        print(search_transactions(transactions, w))

    elif choice == "11":
        date = datetime.strptime(input("Date: "),"%Y-%m-%d" ).date()        
        category = input("Category: ")
        transaction_type = input("Type: ")
        amount = float(input("Amount: "))
        description = input("Description: ")

        transaction = {
            "date": date,
            "category": category,
            "type": transaction_type,
            "amount": amount,
            "description": description
        }
        add_transaction(transactions, transaction)
        save_transactions(transactions, filename)
        print("Transaction added!")

    elif choice == "12":
        i=int(input("Delete: "))
        delete_transaction(transactions, i)
        save_transactions(transactions, filename)
        print("Transaction deleted!")

    elif choice == "13":
        report = generate_report(transactions)
        save_report(report, "data/report.txt")
        print(report)
        print("Report saved!")

    elif choice == "0":
        break