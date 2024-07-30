n=int(input("enter num: "))
a,b=0,1
sum=a
for _ in range(n-1):
    a,b=b,a+b
    sum+=a
print(n,sum)
