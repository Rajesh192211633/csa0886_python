s = "(){}[]"
stack = []
mapping = {")": "(", "}": "{", "]": "["}
valid = True
for char in s:
    if char in mapping:
        top_element = stack.pop() if stack else '#'
        if mapping[char] != top_element:
            valid = False
            break
    else:
        stack.append(char)
print(valid)
