#!/usr/bin/python
"""
Given two strings, find the longest common substring.

Return the length of it.
"""
class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        # write your code here
        n = len(A)
        m = len(B)

        # initialize table and result
        t = [ [0 for j in xrange(m+1)] for i in xrange(n+1) ]
        result = 0

        for i in xrange(n+1):
            for j in xrange(m+1):

                # trivial case
                if i == 0 or j == 0:
                    t[i][j] = 0

                # get length at current position
                elif A[i-1] == B[j-1]:
                    t[i][j] = t[i-1][j-1] + 1
                    
                    # compare to previous max-length
                    result = max(result, t[i][j])

                else:
                    t[i][j] = 0

        return result

# test
if __name__ == '__main__':
    test = Solution()
    A = "ABCBCD"
    B = "CBCE"
    print test.longestCommonSubstring(A, B)


