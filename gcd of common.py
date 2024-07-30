def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def gcd_of_strings(str1, str2):
    
    if str1 + str2 != str2 + str1:
        return ""
    
    
    gcd_length = gcd(len(str1), len(str2))
    
   
    return str1[:gcd_length]


str1 = "ABABAB"
str2 = "ABAB"
print(gcd_of_strings(str1, str2))  
