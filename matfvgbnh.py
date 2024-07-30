a=[[1,2,3],
   [4,5,6]]
while a:
    print(*(a.pop(0)),end=" ")
    a=list(zip(*a))[::-1]
