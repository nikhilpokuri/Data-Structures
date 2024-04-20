#number of possibilities to reach the given target using 3,5,10
def count(target) -> int:
    lib = [0]*(target+1)
    lib[0] = 1
    for num in [3,5,10]:
        for i in range(num,target+1):
            if lib[i-num]:
                lib[i] += lib[i-num]
    return lib[target]
print(count(10))