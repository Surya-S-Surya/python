def credit(cus,accountno):
    for idd in cus:
        if idd[1]==accountno:
            print("Account number found")
            print()
            creditamount=int(input("Enter amount to credit "))
            
            idd[2]=idd[2]+creditamount
            print("amount credited successfully")
            print("\nname: \t\t",idd[0],"\naccount number: ",idd[1],"\nbalance:\t",idd[2])
            print()
            break
        else:
            print("Invalid account number")
            break
    





    
def debit(cus,accountno):
    for idd in cus:
        if idd[1]==accountno:
            print("Account number found")
            print()
            debitamount=int(input("Enter amount to debit "))
            if idd[2]>debitamount:
                idd[2]=idd[2]-debitamount
                print("amount debitted successfully")
                print("\nname: \t\t",idd[0],"\naccount number: ",idd[1],"\nbalance:\t",idd[2])
                break
            else:
                print("Not enough money Bruhh!!\n")
        else:
            print("Invalid account number")
            break
    


    
def ordered(cus):
    length=len(cus)
    for i in range(length):
        for j in range(0,length-i-1):
            if cus[j][2]>cus[j+1][2]:
                cus[j],cus[j+1]=cus[j+1],cus[j]
    print("Ordered details")
    for i in cus:
        print("\nname: \t\t",i[0],"\naccount number: ",i[1],"\nbalance:\t",i[2])





































    





    
