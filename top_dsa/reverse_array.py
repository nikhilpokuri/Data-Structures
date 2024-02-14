arr = [2,4,-1,5,-9,-4]
start = 0
end = len(arr)-1

while start<end:
    arr[start],arr[end] = arr[end],arr[start]
    start += 1
    end -= 1
print(arr)