#!/usr/bin/python
"""
Given an array of integers, find a contiguous subarray which has the largest sum.
"""
class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        import sys
        
        max_sum = - sys.maxint
        sum = 0

        n = len(nums)
        
        for i in xrange(n):
            sum += nums[i]
            max_sum = max(max_sum, sum)    
            if sum < 0:
                sum = 0
                
        return max_sum

if __name__ == '__main__':

    a = [-2,2,-3,4,-1,2,1,-5,3]  # 6
    print Solution().maxSubArray(a)
