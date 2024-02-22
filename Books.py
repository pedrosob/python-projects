total_books = 0
high_ranking_books = 0
medium_ranking_books = 0
low_ranking_books = 0
add_more = "y"

while add_more == "y":
    book = input("Enter a favorite book: ")
    total_books = total_books + 1

    rank = int(input("Rank the book on a scale of 1 to 10 (1 being the lowest, 10 being the highest): "))

    if 1 <= rank <= 3:
        low_ranking_books = low_ranking_books + 1
    elif 4 <= rank <= 7:
        medium_ranking_books = medium_ranking_books + 1
    else:
        high_ranking_books = high_ranking_books + 1

    add_more = input("Do you want to add more (Y/N)? ").lower()

print("You entered", total_books, "books altogether.")
print("There were", high_ranking_books, "books with a high ranking (8-10).")
print("There were", medium_ranking_books, "books with a medium ranking (4-7).")
print("There were", low_ranking_books, "books with a low ranking (1-3).")

