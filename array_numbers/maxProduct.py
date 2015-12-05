#!/usr/bin/python
"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.
"""
class Solution:
    # @param nums: an integer[]
    # @return: an integer
    def maxProduct(self, nums):
        # write your code here
        import sys
        
        max_prod = - sys.maxint
        max_cur, min_cur = 1, 1
        n = len(nums)
        
        for i in xrange(n):
            a = nums[i]

            # update concurrently            
            tmp1 = max_cur
            tmp2 = min_cur
            max_cur = max(tmp1*a, tmp2*a, a)
            min_cur = min(tmp1*a, tmp2*a, a)
            
            max_prod = max(max_prod, max_cur)
            
        return max_prod
        
if __name__ == '__main__':
    a = [2,3,-2,4]  # 6
    print Solution().maxProduct(a)
