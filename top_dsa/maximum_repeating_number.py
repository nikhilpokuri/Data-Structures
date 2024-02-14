def maxRepeating(arr):
    lib = {}
    for i in arr:
        if i in lib:
            lib[i] += 1
        else:
            lib[i] = 1
    maxi = max(lib.values())
    res = []
    for i in lib:
        if lib[i] == maxi:
            res.append(i)
    return sorted(res)[0]
print(maxRepeating([1,2,3,1,2]))