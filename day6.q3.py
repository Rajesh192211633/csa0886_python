s = "PAYPALISHIRING"
numRows = 3

if numRows == 1 or numRows >= len(s):
    print(s)


rows = [''] * numRows
current_row = 0
going_down = False


for char in s:
    rows[current_row] += char
    if current_row == 0 or current_row == numRows - 1:
        going_down = not going_down
    current_row += 1 if going_down else -1


result = ''.join(rows)
print(result)  
