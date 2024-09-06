n=int(input("enter the number "))
factors=[]
for i in range(1,n+1):
    if n%i==0:
        factors.append(i)
    else:
        pass
print("Factors of ",n," is ",factors)
m=0
primefactors=[]
for k in range(len(factors)):
    prime=True
    m=factors[k]
    if m==1:
        pass
        prime=False
    elif m>1:
        for i in range(2,m):
            if m%i==0:
                prime=False
                break
            else:
                prime=True
    else:
        pass
    if prime:
        primefactors.append(m)
    else:
        pass

print("Prime Factors of ",n," is ",primefactors)  
