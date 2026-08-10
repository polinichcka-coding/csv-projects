from datetime import datetime

def read_transactions(filename):
    with open(filename) as file:
        data=file.read()

    lines=data.splitlines()
    transactions=[]
    for line in lines[1:]:
        parts=line.strip().split(",")
        transaction={
            "date": datetime.strptime(parts[0], "%Y-%m-%d").date(),
            "category": parts[1],
            "type": parts[2],
            "amount": float(parts[3]),
            "description": parts[4]
        }
        transactions.append(transaction)
    return transactions

def save_transactions(transactions, filename):
    with open(filename, "w") as file:
        file.write("date,category,type,amount,description\n")
        for tr in transactions:
            file.write(f"{tr['date']},{tr['category']},{tr['type']},{tr['amount']},{tr['description']}\n")
