#!/usr/bin/python
"""
Given an array of integers, find two non-overlapping subarrays which have the largest sum.

The number in each subarray should be contiguous.

Return the largest sum.
"""
class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        # write your code here    
        import sys
        
        n = len(nums)

        sum, max_sum = 0, - sys.maxint
        L_max = [0 for i in xrange(n)]
        for i in xrange(n):
            sum += nums[i]
            max_sum = max(max_sum, sum)
            L_max[i] = max_sum
            sum = max(sum, 0)
            
        sum, max_sum = 0, - sys.maxint
        R_max = [0 for i in xrange(n)]
        for i in xrange(n-1,-1,-1):
            sum += nums[i]
            max_sum = max(max_sum, sum)
            R_max[i] = max_sum
            sum = max(sum, 0)
            
        max_sum = - sys.maxint
        for i in xrange(n-1):
            max_sum = max(max_sum, L_max[i] + R_max[i+1])
            
        return max_sum

if __name__ == '__main__':
    a = [1,3,-1,2,-1,2]  # 7
    print Solution().maxTwoSubArrays(a)
