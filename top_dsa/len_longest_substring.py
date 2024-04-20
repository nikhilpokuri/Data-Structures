def lengthOfLongestSubstring(s):
    lib = set()
    left = 0
    right = 0
    curr_max = 0
    while right < len(s):
        if s[right] not in lib:
            curr_max = max(curr_max, (right-left) + 1)
            lib.add(s[right])
            right += 1
        else:
            while s[right] in lib:
                lib.remove(s[left])
                left += 1
    return curr_max
print(lengthOfLongestSubstring('abcdea'))