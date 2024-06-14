def maxSubStr(s):
    left = 0
    right = 0

    lib = set()
    res_cnt = 0
    res_str = ""
    while right < len(s):
        if s[right] not in lib:
            res_cnt = max(res_cnt, (right-left) + 1)
            res_str = max(res_str, s[left:right+1], key=lambda x:len(x))
            lib.add(s[right])
            right += 1
        else:
            while s[right] in lib:
                lib.remove(s[left])
                left += 1
    return res_cnt, res_str
string = input("Enter String: ")
print(maxSubStr(string))