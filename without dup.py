lst1=[1,2,3]
lst2=[1,3,4]
merge=sorted(lst1+lst2)
without_dup=list(set(merge))
print(without_dup)
