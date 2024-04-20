def trappingWater(arr,n):
    lef, rig = [0 for _ in arr], [0 for _ in arr]
    lef[0] = arr[0]
    for i in range(1,n):
        lef[i] = max(arr[i], lef[i-1])
    
    rig[n-1] = arr[n-1]   
    for j in range(n-2, -1, -1):
        rig[j] = max(arr[j], rig[j+1])

    res = 0
    for k in range(n):
        res += min(lef[k], rig[k]) - arr[k]
    return res
print(trappingWater([8,8,2,4,5,5,1],7))