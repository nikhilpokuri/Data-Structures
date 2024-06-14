def combinations(n, k):
    res = []
    def backtrack(i, tmp:list):
        if len(tmp) == k:
            res.append(tmp.copy())
            return
        for num in range(i, n+1):
            tmp.append(num)
            backtrack(num+1, tmp)
            tmp.pop()
    backtrack(1, [])
    return res
n = int(input("n: "))
k = int(input("k: "))
print(combinations(n, k))