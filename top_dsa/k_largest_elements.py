import heapq
def k_largest_elements(nums,k):
    res = heapq.nlargest(k,nums)
    return res
print(k_largest_elements([1,2,3,1,2,3],2))