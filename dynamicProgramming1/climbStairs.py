#!/usr/bin/python

"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        
        # initialize table
        A = [1,2] + [0 for i in range(2,n)]
        
        # bottom-up approach
        for i in range(2,n):
            A[i] = A[i-2] + A[i-1]
            
        return A[n-1]

#
if __name__ == "__main__":
    test = Solution()
    n = 3
    print test.climbStairs(n)
