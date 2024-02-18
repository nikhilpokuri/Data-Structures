def maxSubstring(s):
    zero = 0
    one = 0
    maxi = 0
    curr = 0
    for i in s:
        if i == '0':
            zero += 1
        else:
            one += 1
        curr = zero - one
        if curr > maxi:
            maxi = curr
        if curr < 0:
            zero = 0
            one = 0
    if maxi:
        return maxi
    return -1

result = maxSubstring("001111")
print(result)
