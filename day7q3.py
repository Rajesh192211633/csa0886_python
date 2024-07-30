def generateParenthesis(n):
    def backtrack(S, left, right):
        if len(S) == 2 * n:
            combinations.append("".join(S))
            return
        if left < n:
            S.append('(')
            backtrack(S, left + 1, right)
            S.pop()
        if right < left:
            S.append(')')
            backtrack(S, left, right + 1)
            S.pop()
    
    combinations = []
    backtrack([], 0, 0)
    return combinations


print(generateParenthesis(3))  
print(generateParenthesis(1))  
