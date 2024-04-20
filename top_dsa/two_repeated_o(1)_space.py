arr = [1,2,2,1]
n = len(arr)
res = []
for i in range(n):
    ind = abs(arr[i]) 
    if arr[ind] > 0:
        arr[ind] *= -1
    else:
        res.append(ind)
print(res)