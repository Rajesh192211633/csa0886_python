nums = [2, 7, 11, 15]
target = 9
num_map = {}
for i in range(len(nums)):
    diff = target - nums[i]
    if diff in num_map:
        print([num_map[diff], i])
        break
    num_map[nums[i]] = i

