
    h=int(input("Enter the hardness of steel "))
    c=float(input("Enter the carbon content "))
    t=int(input("Enter the tensile strength "))
    if h>50 and c<0.7 and t >5600:
        print("Grade 10")
    elif h>50 and c<0.7 and t<=5600:
        print("Grade 9")
    elif h<=50 and c<0.7 and t >5600:
        print("Grade 8")
    elif h>50 and c>0.7 and t >5600:
        print("Grade 7")
    elif h>50 or c<0.7 or t>5600:
        print("grade 6")
    else:
        print("Grade 5")


tc = int(input("Enter the total number of classes held: "))
a = int(input("Enter the number of classes attended: "))

# Calculating the attendance percentage
p = (a /tc) * 100

# Checking if the student is allowed to sit in the exam
if p>= 75:
    print("You are allowed to sit in the exam ",p)
else:
    print("You are not allowed to sit in the ",p)



name=input("Enter your name ")
g=input("Enter the gender ")
ai=float(input("Enter your annual income "))
d=float(input("Enter your Deduction taxable income "))
tax=0
ti=ai-d
if g=='male':
    if ti<=50000:
        tax=0
    elif ti>50000 and ti<=250000:
        tax=ti*0.05
    elif ti>250000 and ti<500000:
        tax=5000+(ti*0.1)
    elif ti>500000:
        tax=10000+(ti*0.2)
    else:
        print("error")
elif g=='female':
    if ti<=50000:
        tax=0
    elif ti>50000 and ti<=250000:
        tax=ti*0.03
    elif ti>250000 and ti<500000:
        tax=2000+(ti*0.08)
    elif ti>500000:
        tax=7000+(ti*0.15)
    else:
        print("error")
else:
    print("enter male or female")
ec=0.3*tax
tt=tax+ec

print(f"Taxable Income {ti:.2f}")
print(f"Tax on Taxable Income {tax:.2f}")
print(f"Education cess {ec:.2f}")
print(f"Total tax {tt:.2f}")

