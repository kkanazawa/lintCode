#!/usr/bin/python
"""
Given two strings, find the longest common subsequence (LCS).

Your code should return the length of LCS.
"""
class Solution:
    """
    @param A, B: Two strings.
    @return: The length of longest common subsequence of A and B.
    """
    def longestCommonSubsequence(self, A, B):
        # write your code here
        n = len(A)
        m = len(B)
    
        # initialize table
        t = [ [0 for j in xrange(m+1)] for i in xrange(n+1) ]

        # bottom-up
        for i in xrange(n+1):
            for j in xrange(m+1):

                # base case
                if i == 0 or j == 0:
                    t[i][j] = 0

                elif A[i-1] == B[j-1]:
                    t[i][j] = 1 + t[i-1][j-1]

                else:
                    t[i][j] = max( t[i-1][j], t[i][j-1] )

        return t[n][m]

#
if __name__ == '__main__':
    test = Solution()
    A = "ABCD"
    B = "EACB"
    print test.longestCommonSubsequence(A, B)
