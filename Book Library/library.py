def read_books(filename):
    books=[]
    with open(filename) as file:
        data=file.read()
    lines=data.splitlines()
    for line in lines[1:]:
        parts=line.strip().split(",")
        book={
            "title": parts[0],
            "author": parts[1],
            "genre": parts[2],
            "year": int(parts[3]),
            "rating": float(parts[4])
        }
        books.append(book)
    return books

def count_books(books):
    return len(books)

def books_by_genre(books):
    d={}
    for book in books:
        if book["genre"] in d:
            d[book["genre"]]+=1
        else:
            d[book["genre"]]=1
    return d

def books_by_author(books):
    d={}
    for book in books:
        if book["author"] in d:
            d[book["author"]]+=1
        else:
            d[book["author"]]=1
    return d

def highest_rate(books):
    highest=0
    high_book=books[0]
    for i in books:
        if i["rating"]>highest:
            highest=i["rating"]
            high_book=i
    return high_book

def average_rating(books):
    s=0
    for i in books:
        s+=i["rating"]
    return s/len(books)

def filter_by_genre(books, genre):
    l=[]
    for book in books:
        if book["genre"]==genre:
            l.append(book)
    return l

def filter_by_rating(books, rating):
    l=[]
    for book in books:
        if book["rating"]>=rating:
            l.append(book)
    return l

def books_after_year(books, year):
    return [book for book in books if book["year"]>year]

books=read_books("data/text.csv")
print(books)
print(count_books(books))
print(books_by_genre(books))
print(books_by_author(books))
print(highest_rate(books))
print(average_rating(books))
print(filter_by_genre(books, "fantasy"))
print(filter_by_rating(books, 4.7))
print(books_after_year(books, 1990))
