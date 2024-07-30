import os
def prefix(str):
    if not str:
        return ""
    return os.path.commonprefix(str)
print(prefix(["flower", "flow", "flight"]))  
print(prefix(["dog", "racecar", "car"]))     
