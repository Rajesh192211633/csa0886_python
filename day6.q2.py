s = "babad"

start = 0
end = 0

for i in range(len(s)):
    # Odd length palindromes (centered at one character)
    left = i
    right = i
    while left >= 0 and right < len(s) and s[left] == s[right]:
        if right - left > end - start:
            start = left
            end = right
        left -= 1
        right += 1

    # Even length palindromes (centered between two characters)
    left = i
    right = i + 1
    while left >= 0 and right < len(s) and s[left] == s[right]:
        if right - left > end - start:
            start = left
            end = right
        left -= 1
        right += 1

# Print the longest palindromic substring
print(s[start:end + 1])  # Output: "bab" or "aba"
