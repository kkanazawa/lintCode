#!/usr/bin/python
"""
Given an array with integers.

Find two non-overlapping subarrays A and B, which |SUM(A) - SUM(B)| is the largest.

Return the largest difference.
"""
class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two
             Subarrays
    """
    def maxDiffSubArrays(self, nums):
        # write your code here
        import sys
        
        n = len(nums)

        # from left to right
        sum1, max_sum = 0, - sys.maxint
        sum2, min_sum = 0, + sys.maxint
        
        L_max = [0 for i in xrange(n)]
        L_min = [0 for i in xrange(n)]
        
        for i in xrange(n):
            sum1 += nums[i]
            sum2 += nums[i]
            
            max_sum = max(max_sum, sum1)
            min_sum = min(min_sum, sum2)
            
            L_max[i] = max_sum
            L_min[i] = min_sum
            
            sum1 = max(sum1, 0)
            sum2 = min(sum2, 0)
            
        # from right to left
        sum1, max_sum = 0, - sys.maxint
        sum2, min_sum = 0, + sys.maxint
        
        R_max = [0 for i in xrange(n)]
        R_min = [0 for i in xrange(n)]
        
        for i in xrange(n-1,-1,-1):
            sum1 += nums[i]
            sum2 += nums[i]
            
            max_sum = max(max_sum, sum1)
            min_sum = min(min_sum, sum2)
            
            R_max[i] = max_sum
            R_min[i] = min_sum
            
            sum1 = max(sum1, 0)
            sum2 = min(sum2, 0)
        
        # get the max sum of two non-overlapping subarrays
        max_sum = - sys.maxint
        for i in xrange(n-1):
            tmp1 = abs(L_min[i]-R_max[i+1])
            tmp2 = abs(L_max[i]-R_min[i+1])
            max_sum = max( max_sum, tmp1, tmp2 )

        return max_sum
            
if __name__ == '__main__':
    a = [1,2,-3,1]  # 6
    print Solution().maxDiffSubArrays(a)
            
