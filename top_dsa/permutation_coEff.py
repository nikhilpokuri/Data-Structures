def permutationCoeff(n, k):
    res = 1
    for i in range(k):
        res *= (n-i)
    return res%((10**9)+7)
print(permutationCoeff(10,3))