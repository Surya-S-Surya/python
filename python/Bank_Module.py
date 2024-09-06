def customerdetails():
    n=int(input("Enter no of custormer "))
    c=[]
    for i in range(n):
        
        name=input("Enter name ")
        acc=int(input("Enter acc no "))
        bal=int(input("Enter balance amount "))
        print()
        c.append([name,acc,bal])
    return c
