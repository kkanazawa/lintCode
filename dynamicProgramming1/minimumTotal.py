#!/usr/bin/python

"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
"""

class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    def minimumTotal(self, triangle):
        # write your code here
        
        # initialize table
        m = len(triangle)
        A = [[0]*i for i in xrange(1,m+1)]
        A[0][0] = triangle[0][0]
        
        # bottom-up approach
        for i in xrange(1,m):
            A[i][0] = triangle[i][0] + A[i-1][0]
            A[i][-1] = triangle[i][-1] + A[i-1][-1]
            
        for i in xrange(2,m):
            for j in range(1,i):
                A[i][j] = min( A[i-1][j], A[i-1][j-1] ) + triangle[i][j]
                
        return min(A[-1])

#
if __name__ == "__main__":
    test = Solution()
    triangle = [ [2], [3,4], [6,5,7], [4,1,8,3] ]
    print test.minimumTotal(triangle)
    
