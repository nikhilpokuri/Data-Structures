lib = {}
def ncr(n,r):
    def fact(n):
        if n <= 1:
            return 1
        if n == 2:
            return 2
        if n in lib:
            return lib[n]
        lib[n] = n * fact(n-1)
        return lib[n]
    return fact(n) // (fact(r) * fact(n-r))
print(ncr(10,3))