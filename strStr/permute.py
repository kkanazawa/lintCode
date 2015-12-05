#!/usr/bin/python

"""
Given a list of numbers, return all possible permutations
"""

class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        
        # detect null
        if nums is None:
            return []
        
        # base case
        elif len(nums) <= 1:
            return [nums]
        
        # recursion
        else:
            result = []
            n = len(nums)
            
            for i in xrange(n):
                first = [nums[i]]
                A_sub = nums[:i] + nums[i+1:]
                
                rest = self.permute(A_sub)
                
                for j in rest:
                    temp = first + j
                    result.append(temp)
                    
            return result

#
if __name__ == "__main__":
    test = Solution()
    A = [1,2,3]
    print test.permute(A)
