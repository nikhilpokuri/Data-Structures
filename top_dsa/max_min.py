arr = [2,3,1]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] > arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
print('max and min:',arr[0],arr[-1])
print('max_min sum:',arr[0]+arr[-1])
