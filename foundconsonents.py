input=str(input("enter string : "))
vowels='aeiouAEIOU'
output=[char for char in input if char not in vowels]
print(output)
