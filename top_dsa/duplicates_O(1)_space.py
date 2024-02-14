def find_duplicates(arr):
	duplicates = []
	n = len(arr)
	for i in range(n):
		index = arr[i] % n
		arr[index] += 10
		
	for i in range(n):
		if arr[i] // 10 >= 2:
			duplicates.append(i)
	return duplicates


arr = [1,2,1,3,4,3]
print("The repeating elements are:")
ans = find_duplicates(arr)
for x in ans:
	print(x, end=" ")
