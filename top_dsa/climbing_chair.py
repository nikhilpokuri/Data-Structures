def climb(n):
    lib = [0]*(n+1)
    lib[n] = 1
    lib[n-1] = 1
    for i in range(n-2,-1,-1):
        lib[i] = lib[i+1] + lib[i+2]
    return lib[0]
print(climb(3))