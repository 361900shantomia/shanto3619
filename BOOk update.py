def update_book():
    view_books()
    books = load_books()
    if not books:
        return
    try:
        index = int(input("Enter the book number to update: ")) - 1
        if 0 <= index < len(books):
            print("\nUpdating Book Information:")
            books[index]["title"] = input(f"New Title ({books[index]['title']}): ") or books[index]["title"]
            books[index]["authors"] = input(f"New Authors ({books[index]['authors']}): ") or books[index]["authors"]
            books[index]["isbn"] = input(f"New ISBN ({books[index]['isbn']}): ") or books[index]["isbn"]
            books[index]["year"] = input(f"New Year ({books[index]['year']}): ") or books[index]["year"]
            books[index]["price"] = float(input(f"New Price ({books[index]['price']}): ") or books[index]["price"])
            books[index]["quantity"] = int(input(f"New Quantity ({books[index]['quantity']}): ") or books[index]["quantity"])
            save_books(books)
            print("Book updated successfully!")
        else:
            print("Invalid book number!")
    except ValueError:
        print("Invalid input!")
