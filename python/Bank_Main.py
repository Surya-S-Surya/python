import Bank_Module
import Bank_Transaction

def Bank():
    cus=Bank_Module.customerdetails()
    k=0
    while k<1:
        inp=input("\n\nEnter 1 for credit, 2 for debit, 3 ordered, 4 to exit")
        print()

        if inp=='1':
            accountno=int(input("enter the account number to credit "))
            print()
            Bank_Transaction.credit(cus,accountno)
            
            
        elif inp=='2':
            accountno=int(input("enter the account number to debit "))
            print()
            Bank_Transaction.debit(cus,accountno)
            
        elif inp=='3':
            Bank_Transaction.ordered(cus)
        elif inp=='4':
            k=10
            print("Go fuck yourself")
        else:
            print("invalid")

if __name__=='__main__':
    Bank()
    print("Easy program(I'm so fucked up doing this shit!!)")
            
