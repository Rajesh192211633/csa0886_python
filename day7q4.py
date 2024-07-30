def divide(dividend, divisor):
    if dividend == 0:
        return 0
    if divisor == 0:
        raise ValueError("Divisor cannot be zero.")
    
    negative = (dividend < 0) ^ (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)
    
    quotient = 0
    while dividend >= divisor:
        temp, multiple = divisor, 1
        while dividend >= temp:
            dividend -= temp
            quotient += multiple
            temp <<= 1
            multiple <<= 1
    
    if negative:
        quotient = -quotient
    
    return max(min(quotient, 2147483647), -2147483648)

# Test Cases
print(divide(10, 3))
print(divide(7, -3))  
