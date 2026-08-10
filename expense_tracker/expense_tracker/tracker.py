def read_expenses(filename):
    expenses = []
    with open(filename) as file:
        data = file.read()
    lines = data.splitlines()
    for line in lines[1:]:
        parts = line.strip().split(",")
        expense = {
            "date": parts[0],
            "category": parts[1],
            "amount": float(parts[2])
        }

        expenses.append(expense)
    return expenses

def total_expenses(expenses):
    total=0
    for expense in expenses:
        total+=expense["amount"]
    return total

def expenses_by_category(expenses):
    d={}
    for expense in expenses:
        category=expense["category"]
        amount=expense["amount"]
        if category in d:
            d[category]+=amount
        else:
            d[category]=amount
    return d

def max_purchase(expenses):
    maxim=expenses[0]
    for expense in expenses:
        if expense["amount"]>maxim["amount"]:
            maxim=expense
    return maxim

def average_expense(expenses):
    count=0
    for expense in expenses:
        count+=1
    ave=total_expenses(expenses)/count
    return ave

def most_expensive_category(expenses):
    cat=expenses_by_category(expenses)
    max_category=""
    max_amount=0
    for category in cat:
        if cat[category] > max_amount:
            max_amount=cat[category]
            max_category=category
    return max_category

def filter_expenses(expenses, s):
    l=[]
    for expense in expenses:
        if expense["amount"]>s:
            l.append(expense)
    return l


expenses = read_expenses("sample_data/expenses.csv")
print(expenses)
print(total_expenses(expenses))
print(expenses_by_category(expenses))
print(max_purchase(expenses))
print(average_expense(expenses))
print(most_expensive_category(expenses))
print(filter_expenses(expenses, 10))