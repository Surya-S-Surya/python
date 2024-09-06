def addbook(database):
    yestitle=True
    title=input("Enter book title ")
    for item in database:
        if item[0]==title:
            yestitle=False
        else:
            pass
        
    if not yestitle:
        print("That book title is already present")
        
    if yestitle:
        author=input("Enter book author ")
        price=int(input("Enter book price "))
        publ=input("Enter book publisher ")
        books=int(input("Enter no of books "))
        database.append([title,author,price,publ,books])

        
def displaybook(database):
    for item in database:
        print("\nTitle:   ",item[0],"\nAuthor:    ",item[1],"\nPrice:    ",item[2],"\nPublisher: ",item[3],"\nBooks:    ",item[4])
    
def removebook(database):
    getbook=input("Enter the book title to remove the book ")
    yesbook=True
    for item in database:
        if item[0]==getbook:
            print('book found\n')
            rembook=int(input("Enter no of books to remove "))
            if rembook<=item[-1]:
                item[-1]=item[-1]-rembook
                print("\nBooks were removed successfully")
            else:
                print("\ninvalid to remove books")
        else:
            yesbook=False
    if not yesbook:
        print("\nBook title not found")
        
def deletebook(database):
    getbook=input("\nEnter the book title to delete")
    for item in database:
        if item[0]==getbook:
            print("Database of book title is found and deleted successfully")
            database.remove(item)
        else:
            print("Book not found\n")
database=[]
k=0
while k<1:

    print("\nEnter 1 to add book, 2 to display. 3 to remove, 4 to delete, 5 to exit")
    inp=int(input())

    if inp==1:
        addbook(database)
        
        
    elif inp==2:
        displaybook(database)
        
    elif inp==3:
        removebook(database)
        
    elif inp==4:
        deletebook(database)
        
    elif inp==5:
        print("Get lost MF")
        k=10
        
    else:
        print("Enter the valid number u dumb ass..")
