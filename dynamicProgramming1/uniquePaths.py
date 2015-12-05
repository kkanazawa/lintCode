#!/usr/bin/python

"""
A robot is located at the top-left corner of a m x n grid.

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid.

How many possible unique paths are there?
"""

class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """ 
    def uniquePaths(self, m, n):
        # write your code here
        
        # initialize table
        A = [ [ i for i in xrange(n) ] for j in xrange(m) ] 
        
        # bottom up
        for i in xrange(m):
            A[i][0] = 1
            i += 1
            
        for i in xrange(n):
            A[0][i] = 1
            i += 1
            
        for i in xrange(1,m):
            
            for j in xrange(1,n):
                A[i][j] = A[i-1][j] + A[i][j-1]
                
        return A[m-1][n-1]
            

#
if __name__ == "__main__":
    test = Solution()
    m, n = 4, 3
    print test.uniquePaths(m, n)
