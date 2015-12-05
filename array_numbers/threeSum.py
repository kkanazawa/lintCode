#!/usr/bin/python
"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
"""
class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    # time: O(n^2)
    def threeSum(self, numbers):
        # write your code here
        n = len(numbers)
        d = dict([(j,i) for i,j in enumerate(numbers)])

        res = []
        for i in xrange(n):
            for j in xrange(i,n):
                if i!=j and d.get(-numbers[i]-numbers[j], None) not in [i,j,None]:
                    i1 = numbers[i]
                    i2 = numbers[j]
                    i3 = numbers[d.get(-numbers[i]-numbers[j])]
                    tmp = sorted([i1,i2,i3])
                    if tmp not in res:
                        res.append(tmp)
            
        return res

if __name__ == '__main__':
    a = [-1,0,1,2,-1,4]
    print Solution().threeSum(a)
