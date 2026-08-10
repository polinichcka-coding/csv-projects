from tracker.io import read_transactions

def total_income(transactions):
    s=0
    for tr in transactions:
        if tr["type"]=="income":
            s+=tr["amount"]
    return s

def total_expenses(transactions):
    s=0
    for tr in transactions:
        if tr["type"]=="expense":
            s+=tr["amount"]
    return s

def balance(transactions):
    a=total_income(transactions)
    b=total_expenses(transactions)
    return a-b

def expenses_by_category(transactions):
    d={}
    for tr in transactions:
        if tr["type"] == "expense":
            if tr["category"] in d:
                d[tr["category"]]+=tr["amount"]
            else:
                d[tr["category"]]=tr["amount"]
    return d

def biggest_expense(transactions):
    big=None
    for tr in transactions:
        if tr["type"]=="expense":
            if big is None or tr["amount"]>big["amount"]:            
                big=tr
    return big

def average_expense(transactions):
    expenses = []
    for tr in transactions:
        if tr["type"]=="expense":
            expenses.append(tr["amount"])
    if not expenses:
        return 0
    return sum(expenses)/len(expenses)

def filter_by_category(transactions, category):
    l=[]
    for tr in transactions:
        if tr["category"]==category:
            l.append(tr)
    return l

def filter_by_date(transactions, start, end):
    l=[]
    for tr in transactions:
        if start <= tr["date"] <= end:
            l.append(tr)
    return l

def search_transactions(transactions, word):
    l=[]
    for tr in transactions:
        if word.lower() in tr["description"].lower():
            l.append(tr)
    return l


