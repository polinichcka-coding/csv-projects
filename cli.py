from analyzer import(
    count_lines,
    count_words,
    unique,
    often,
    max_length,
    average, 
    frequency
)

with open("sample_data/text.txt") as file:
    text = file.read()

while True:
    print(
    """
    1. Count lines
    2. Count words
    3. Unique
    4. Often
    5. Max length
    6. average
    7. frequency
"""
    )

    choice = input("Choose an option: ")

    if choice=="1":
        print(count_lines(text))

    elif choice=="2":
        print(count_words(text))

    elif choice=="3":
        print(unique(text))

    elif choice=="4":
        print(often(text))

    elif choice=="5":
        print(max_length(text))

    elif choice=="6":
        print(average(text))

    elif choice=="7":
        print(frequency(text))

    elif choice=="0":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")