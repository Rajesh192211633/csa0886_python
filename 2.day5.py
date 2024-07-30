def roman_to_integer(s):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    
    for char in s:
        value = roman_values[char]
        total += value if value <= prev_value else value - 2 * prev_value
        prev_value = value
    
    return total


s = "III"
print(roman_to_integer(s))  
