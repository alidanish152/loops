"""for i in range(0,4,1):
    print("ali danish")
for i in range(0,20,2):
    print(i)
tno=int(input("enter a number"))
for i in range(1,12):
    print(tno,"*",i,"=",tno*i)
n=int(input("enter a number"))
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1
print(sum)"""
n=int(input("enter the number of rows"))
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
