#!/usr/bin/python
"""
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are NOT zero-based.
"""
class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    # time: O(n^2)
    def twoSum(self, numbers, target):
        # write your code here
        n = len(numbers)
        for i in xrange(n):
            for j in xrange(i,n):
                if i!=j and numbers[i]+numbers[j] == target:
                    return [i+1, j+1]

        return -1

    # time: O(n)
    def twoSum2(self, numbers, target):
        # write your code here
        n = len(numbers)
        
        d = dict([(j,i) for i,j in enumerate(numbers)])
        for i in xrange(n):
            if d.get(target-numbers[i], -1) != -1:
                return sorted([i + 1, d.get(target-numbers[i]) + 1 ])

        return -1

    # lookup by values
    def twoSum(self, numbers, target):
        # write your code here
        n = len(numbers)



if __name__ == '__main__':
    a = [2,7,11,15]
    t = 9
    print Solution().twoSum(a,t)
