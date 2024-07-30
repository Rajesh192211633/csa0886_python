import itertools
def permute(nums):
    return list(itertools.permutations(nums))
print(permute([1, 2, 3]))


from itertools import permutations
def permuteUnique(nums):
    return list(set(permutations(nums)))
print(permuteUnique([1,1,2]))
