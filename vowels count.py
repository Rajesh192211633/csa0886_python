input=str(input("enter the number: "))
vowels='aeiouAEIOU'
count=0
for char in input:
    if char in vowels:
        count+=1
print(count)        
