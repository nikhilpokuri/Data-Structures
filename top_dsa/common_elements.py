def commonElements (A, B, C, n1, n2, n3):
    a = set(A)
    b = set(B)
    c = set(C)
    res = []
    for i in a:
        if i in b and i in c:
            res.append(i)
    if res:
        res.sort()
        return res
    return [-1]
print(commonElements([1,2,3,4],[2,3,5],[2,3,4,6],4,3,4))