def topKFrequent(nums, k):
    lib = {}
    for i in nums:
        if i in lib:
            lib[i] += 1
        else:
            lib[i] = 1
    res = sorted(lib,key=lambda x: lib[x],reverse=True)
    return res[:k]
print(topKFrequent([1,1,2,3,2],2))