#!/usr/bin/python

"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

"""
class Solution:
    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        
        # useful parameters
        m = len(grid)
        n = len(grid[0])
        
        # initialize table
        T = [[0 for j in range(n)] for i in range(m)]
        T[0][0] = grid[0][0]
        
        # bottom-up
        for i in range(1,m):
            T[i][0] = grid[i][0] + T[i-1][0]
            
        for j in range(1,n):
            T[0][j] = grid[0][j] + T[0][j-1]
            
        for i in range(1,m):
            for j in range(1,n):
                T[i][j] = grid[i][j] + min(T[i-1][j], T[i][j-1])
                
        return T[m-1][n-1]

#
if __name__ == "__main__":
    test = Solution()
    grid = [[1,2,3], [2,3,4], [3,4,5]]
    print test.minPathSum(grid)

