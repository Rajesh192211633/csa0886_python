def mySqrt(x: int) -> int:
    left, right = 0, x
    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= x < (mid + 1) * (mid + 1):
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1


print(mySqrt(4))
print(mySqrt(8))   
print(mySqrt(0))   
print(mySqrt(1))   
print(mySqrt(16))  
print(mySqrt(27))  
