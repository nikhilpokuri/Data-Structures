def search(nums, target):
        if len(nums) == 1 and nums[0]==target:
            return 0
        """
            store the 1st element and find the max comparing with 1st, 
               while doing it find if you found the target and return index
        """
        maxi = nums[0] #1st element
        if maxi == target: #checking if the 1st element is target
            return 0
        large_ind = 1
        while large_ind < len(nums) and nums[large_ind] > maxi :
            if nums[large_ind] == target:
                return large_ind
            maxi = nums[large_ind]
            large_ind += 1

        """since it is rotated sort array, the target smaller than max will be found after max element"""
        if target < maxi:
            small_ind = large_ind
            while small_ind < len(nums):
                if nums[small_ind] == target:
                    return small_ind
                small_ind += 1
        return -1
nums1 = [4,5,6,7,0,1,2]
target1 = 0

nums2 = [1,2,3]
target2 = 1

nums3 = [1,2]
target3 = 2

print(search(nums1,target1))