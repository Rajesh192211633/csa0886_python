def get_row(rowIndex):
    row = [1] * (rowIndex + 1)
    for k in range(1, rowIndex):
        row[k] = row[k - 1] * (rowIndex - k + 1) // k
    return row


rowIndex = 3
print(get_row(rowIndex))  
