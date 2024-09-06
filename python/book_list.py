def add(book_list):
    title = input("Enter book title: ")
    found = False
    
    for book in book_list:
        if book[1] == title:
            count = int(input("Enter the number of books to add: "))
            book[-1] += count
            print("Updated book count.")
            found = True
            break
    
    if not found:
        author = input("Enter author: ")
        price = float(input("Enter price: "))
        publisher = input("Enter publisher: ")
        count = int(input("Enter the number of books: "))
        book_list.append([author, title, price, publisher, count])
        print("Book added.")

def display(book_list):
    print("\nBook Details:")
    for book in book_list:
        print("Author:", book[0])
        print("Title:", book[1])
        print("Price:", book[2])
        print("Publisher:", book[3])
        print("Count:", book[4])
        print()

def remove(book_list):
    title = input("Enter book title to remove: ")
    found = False
    
    for book in book_list:
        if book[1] == title:
            count = int(input("Enter the number of books to remove: "))
            if count <= book[-1]:
                book[-1] -= count
                print("Books removed.")
                if book[-1] == 0:
                    book_list.remove(book)
                    print("Book removed from database.")
            else:
                print("Insufficient books in stock.")
            found = True
            break
    
    if not found:
        print("Book not found in database.")

def delete(book_list):
    title = input("Enter book title to delete: ")
    found = False
    
    for book in book_list:
        if book[1] == title:
            book_list.remove(book)
            print("Book deleted from database.")
            found = True
            break
    
    if not found:
        print("Book not found in database.")

def main():
    book_list = []
    
    while True:
        print("\nBook Store Menu:")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Remove Books")
        print("4. Delete Book")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            add(book_list)
        elif choice == 2:
            display(book_list)
        elif choice == 3:
            remove(book_list)
        elif choice == 4:
            delete(book_list)
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
