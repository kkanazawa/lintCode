#!/usr/bin/python

"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.
"""

class Solution:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        
        # useful parameters
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        # initialize table for bottom-up approach
        A = [ [0 for j in xrange(n)] for i in range(m) ]
        
        # left edge of table
        for i in xrange(m):
            
            if obstacleGrid[i][0] == 0:
                A[i][0] = 1
                i += 1
            # can't go beyond obstacle
            else:
                break

        # top edge of table
        for j in xrange(n):
            
            if obstacleGrid[0][j] == 0:
                A[0][j] = 1
                j += 1
                
            else:
                break
            
        # non edge
        for i in xrange(1,m):
            for j in xrange(1,n):
                
                if obstacleGrid[i][j] == 1:
                    A[i][j] = 0
                else:
                    A[i][j] = A[i-1][j] + A[i][j-1]
        
        return A[m-1][n-1]

#
if __name__ == "__main__":
    test = Solution()
    obstacle = [[0,0,0], [0,1,0], [0,0,0]]
    print test.uniquePathsWithObstacles(obstacle)
