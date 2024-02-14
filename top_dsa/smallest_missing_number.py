arr = [-1,2,5,10,3,9]
n = len(arr)
arr1 = set(arr)
for i in range(1,n):
    if i not in arr1:
        print(i)
        break
else:
    print(-1)