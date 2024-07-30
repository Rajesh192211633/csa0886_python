s = "abcabcbb"

# Initialize variables
char_map = {}
left = 0
max_length = 0

# Traverse the string
for right in range(len(s)):
    if s[right] in char_map:
        left = max(char_map[s[right]] + 1, left)
    char_map[s[right]] = right
    max_length = max(max_length, right - left + 1)

print(max_length)  # Output: 3
