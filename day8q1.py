from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)
    for s in strs:
        sorted_s = ''.join(sorted(s))
        anagrams[sorted_s].append(s)
    return list(anagrams.values())


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  
print(groupAnagrams([""]))  
