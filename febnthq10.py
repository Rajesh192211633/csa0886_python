n=int(input("enter the nunm: "))
a,b=0,1
for _ in range(n-1):

    a,b=b,a+b
print(n,a)
