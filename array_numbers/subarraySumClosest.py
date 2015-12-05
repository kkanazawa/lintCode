#!/usr/bin/python
"""

"""

import sys

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    #
    # 2D DP
    # time: O(n^2)
    # space: O(n^2) (very inefficient)
    #
    def subarraySumClosest(self, nums):
        # write your code here
        n = len(nums)
        DP = [ [0 for j in xrange(n+1)] for i in xrange(n) ]
        dist = sys.maxint

        for i in xrange(n):
            for j in xrange(i+1,n+1):

                DP[i][j] = DP[i][j-1] + nums[j-1]

                if abs(DP[i][j]) < dist:
                    i_clos, j_clos = i,j
                    dist = abs(DP[i][j])

        return [i_clos, j_clos-1]

    # time: O(n^2)
    # space: O(n)
    def subarraySumClosest2(self, nums):
        # write your code here
        n = len(nums)
        sum = 0
        s = []
        dist = sys.maxint

        for i in xrange(n):
            sum += nums[i]
            s.append(sum)

            for j in xrange(i):
                if dist > abs(s[i]-s[j]):
                    dist = abs(s[i]-s[j])
                    i_c, j_c = i, j

        return [j_c+1,i_c]

    # time: O(n log n)
    # space: O(n)
    def subarraySumClosest3(self, nums):
        # write your code here
        n = len(nums)
        sum = 0
        s = []
        for i in xrange(n):
            sum += nums[i]
            s.append(sum)

        s = sorted([(j,i) for i,j in enumerate(s)])

        # use the last element as initial value
        dist, idx = s[-1]
        dist = abs(dist)
        i_c, j_c = idx, idx

        for i in xrange(n-1):

            dist = min(dist, abs(s[i][0]-s[i+1][0]), abs(s[i][0]))

            if dist == abs(s[i][0]-s[i+1][0]):
                i_c = min( s[i][1], s[i+1][1] ) + 1
                j_c = max( s[i][1], s[i+1][1] )
                
            elif dist == abs(s[i][0]):
                i_c, j_c = s[i][1], s[i][1]
    
        return [i_c, j_c]

if __name__ == '__main__':
    a = [6,-4,-8,3,1,7]
    a = [-3,1,1,-3,5]
    a = [-10,-2,-3,-100,1,2,3,-1,4]
#    print Solution().subarraySumClosest(a)
#    print Solution().subarraySumClosest2(a)
    print Solution().subarraySumClosest3(a)
