''' THIS METHOD WILL WORK WHERE arr[i] < len(arr)  '''
def find_duplicates(arr):
	duplicates = []
	n = len(arr)
	for i in range(n):
		index = arr[i] % n
		arr[index] += n
	for j in range(n):
		arr[j] //= n
		if arr[j] >= 2:
			duplicates.append(j)
	return duplicates

arr = [1,1,2,3,2,4,4,3,4]
print("The repeating elements are:")
ans = find_duplicates(arr)
for x in ans:
	print(x, end=" ")
