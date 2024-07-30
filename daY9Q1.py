import re

def is_valid_number(s):

    pattern = re.compile(r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$')
    return bool(pattern.match(s))

print(is_valid_number("0")) 
print(is_valid_number("e")) 
