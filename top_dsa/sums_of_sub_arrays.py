arr = [2,3]
#all sub arrays = [[],[2],[3],[2,3]]
s = [0]
for i in range(len(arr)):
    v = len(s)
    for j in range(i+1):
        s.append(s[j]+arr[i])
print(s)