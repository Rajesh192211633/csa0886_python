def addTwoNumbers(l1, l2):
    
    l1.reverse()
    l2.reverse()
    
    carry = 0
    result = []
    
    for x, y in zip(l1, l2):
        sum = carry + x + y
        carry = sum // 10
        result.append(sum % 10)
    
    for x in l1[len(l2):]:
        sum = carry + x
        carry = sum // 10
        result.append(sum % 10)
    
    
    for y in l2[len(l1):]:
        sum = carry + y
        carry = sum // 10
        result.append(sum % 10)
    

    if carry > 0:
        result.append(carry)
    
    

    
    return result


l1 = [2, 4, 3]
l2 = [5, 6, 4]
result = addTwoNumbers(l1, l2)
print(result)  
