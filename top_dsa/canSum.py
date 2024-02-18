def can_Sum(arr,n,lib={}):
    if n in lib:
        return lib[n]
    if n < 0:
        return False
    if n == 0:
        return True
    for num in arr:
        rem = n-num
        if can_Sum(arr,n-num,lib):
            lib[n] = True
            return True
    lib[n] = False
    return False
print(can_Sum([2,3],7))