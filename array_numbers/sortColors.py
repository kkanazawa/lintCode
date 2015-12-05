#!/usr/bin/python
"""

"""
class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    # naive approach
    def sortColors(self, nums):
        # write your code here

        n = len(nums)
        counts = [0,0,0]
        for i in xrange(n):

            if nums[i] not in [0,1,2]:
                return -1
            counts[ nums[i] ] += 1

        nums[:counts[0]] = [0] * counts[0]
        nums[counts[0]:counts[0]+counts[1]] = [1] * counts[1] 
        nums[counts[0]+counts[1]:] = [2] * counts[2]

        return nums

    # one pass algorithm
    def sortColors2(self, nums):
        # write your code here

        last_zero = 0
        first_two = len(nums) -1
        
        #       
        i = 0
        while i <= first_two:
            
            if nums[i] == 2:
                nums[first_two], nums[i] = nums[i], nums[first_two]
                first_two += - 1

            elif nums[i] == 0:
                nums[last_zero], nums[i] = nums[i], nums[last_zero]
                last_zero += 1
                i += 1

            else:
                i += 1

            print nums, last_zero, first_two

        return nums

if __name__ == '__main__':
    a = [1,0,1,2]
    a = [2,0,0,1,2,0,2]
    a = [2,0,2,2,1,2,2,1,2,0,0,0,1]
    a = [0,2,2,2,2,1,0,1,0,0,0,1,0,2,0]
    print Solution().sortColors2(a)
