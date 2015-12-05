#!/usr/bin/python
"""
For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n) time complexity.

If the target number does not exist in the array, return -1.
"""
class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        # write your code here
    
        # useful parameters
        low = 0
        high = len(nums) - 1

        # iterative approach
        while low + 1 <= high:

            mid = (low + high) / 2

            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid

        if nums[low] == target:
            return low
    
        # not found
        else:  
            return -1

#
if __name__ == "__main__":
    test = Solution()
    nums = [1, 2, 3, 3, 4, 5, 10]
    target = 3
    print test.binarySearch(nums, target)
