def findMissingAndRepeatedValues(grid):
        arr = []
        for i in range(len(grid)):
            arr.extend(grid[i])
        del grid
        arr.sort()
        lib = set()
        repeat = 0
        missing = 0
        for i in range(len(arr)):
            if arr[i] in lib:
                repeat = arr[i]
            lib.add(arr[i])
        for i in range(len(arr)):
            if i+1 not in lib:
                missing = i+1

        return [repeat,missing]
print(findMissingAndRepeatedValues([[1,2,3],[2,4,5],[6,7,9]]))