#!/usr/bin/python
"""
Given a list of numbers with duplicate number in it. Find all unique permutations.
"""

class Solution:
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """
    def permuteUnique(self, nums):
        # write your code here
        
        # detect null
        if nums is None:
            return []
        
        # base case
        elif len(nums)<=1:
            return [nums]
            
        # recursion
        else:
            result = []
            n = len(nums)
            
            for i in xrange(n):
                first = [nums[i]]
                nums_sub = nums[:i] + nums[i+1:]
                
                rest = self.permuteUnique(nums_sub)
                
                for j in rest:
                    temp = first + j
                    result.append(temp)
                    
            result2 = []
            for k in result:
                if k not in result2:
                    result2.append(k)
                    
            return result2

if __name__ == "__main__":
    test = Solution()
    nums = [1,2,2]
    print test.permuteUnique(nums)
