def digital_root(num):
    if num == 0:
        return 0
    return 1 + (num - 1) % 9
num = 777
print(digital_root(num))  
