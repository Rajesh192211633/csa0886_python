s = "PAYPALISHIRING"
numRows = 3

if numRows == 1 or numRows >= len(s):
    print(s)

# Initialize the rows
rows = [''] * numRows
current_row = 0
going_down = False

# Traverse the string and add characters to the appropriate row
for char in s:
    rows[current_row] += char
    if current_row == 0 or current_row == numRows - 1:
        going_down = not going_down
    current_row += 1 if going_down else -1

# Combine all rows to form the final string
result = ''.join(rows)
print(result)  # Output: "PAHNAPLSIIGYIR"
