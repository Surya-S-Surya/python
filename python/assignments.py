n=int(input("Enter no of elements "))
l=[]
print("Enter  elemtnt  ")
for i in range(0,n):
   ele=int(input())
   l.append(ele)
print(l)
for i in range(len(l)-1):
    if l[i]>l[i+1]:
        l[i],l[i+1]=l[i+1],l[i]

print(l)
