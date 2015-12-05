#!/usr/bin/python
"""
Given an integer array, find a subarray where the sum of numbers is zero. Your code should return the index of the first number and the index of the last number.
"""

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here        

        n = len(nums)
        
        for i in xrange(n):            
            s = 0

            for j in xrange(i,n):
                s += nums[j]                

                if s == 0:
                    return [i,j]

    def subarraySum2(self, nums):
        # write your code here
        n = len(nums)
        dict = {}
        s = 0
        for i in xrange(n):

            s += nums[i]

            if dict.get(s,'hey') != 'hey':
                return [dict[s], i]
            dict[s] = i
            print dict


if __name__ == '__main__':

    a = [-3, 1, 2, -3, 4]
    a = [-1,1]
    print Solution().subarraySum(a)
    print Solution().subarraySum2(a)
