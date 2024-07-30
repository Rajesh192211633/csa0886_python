num = 777
while num >= 10:
    num = sum(int(digit) for digit in str(num))
print(num)  # Output: 2

