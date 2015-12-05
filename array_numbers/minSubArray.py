#!/usr/bin/python
"""
Given an array of integers, find the subarray with smallest sum.

Return the sum of the subarray.
"""
class Solution:
    """
    @param nums: a list of integers
    @return: A integer denote the sum of minimum subarray
    """
    def minSubArray(self, nums):
        # write your code here
        import sys
        
        n = len(nums)
        
        sum = 0
        min_sum = sys.maxint
        
        for i in xrange(n):
            sum += nums[i]
            min_sum = min(min_sum, sum)
            
            #  we would choose not to add current sum
            if sum > 0: 
                sum = 0
            
        return min_sum

if __name__ == '__main__':

    a = [1,-2,1,-2]
    print Solution().minSubArray(a)
