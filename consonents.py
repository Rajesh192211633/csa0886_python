input=str(input("enter string: "))
vowels='aeiouAEIOU'
count=0
for char in input:
    if char not in vowels:
        count+=1
print(count)
