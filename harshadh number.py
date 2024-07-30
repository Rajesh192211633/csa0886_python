n = 18 
n_str = str(n)
sum= 0
for digit in n_str:
    digit_int = int(digit)
    sum += digit_int
if n % sum == 0:
    print(f"{n} is a Harshad number")
else:
    print(f"{n} is not a Harshad number")
