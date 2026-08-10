from library import (
    read_books,
    count_books,
    books_by_genre,
    books_by_author,
    highest_rate,
    average_rating,
    filter_by_genre,
    filter_by_rating,
    books_after_year
)

books = read_books("data/text.csv")

while True: 
    print("""
1. Count books
2. Books by genre
3. Books by author
4. Highest rated book
5. Average rating
6. Filter by genre
7. Filter by rating
8. Books after year
0. Exit
""")
    choice=input("Choose: ")

    if choice == "1":
        print(count_books(books))
    elif choice == "2":
        print(books_by_genre(books))
    elif choice == "3":
        print(books_by_author(books))
    elif choice == "4":
        print(highest_rate(books))
    elif choice == "5":
        print(average_rating(books))
    elif choice == "6":
        genre = input("Genre: ")
        print(filter_by_genre(books, genre))
    elif choice == "7":
        rating = float(input("Rating: "))
        print(filter_by_rating(books, rating))
    elif choice == "8":
        year = int(input("Year: "))
        print(books_after_year(books, year))
    elif choice == "0":
        break
    else:
        print("Invalid choice")