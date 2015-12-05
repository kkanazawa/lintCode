#!/usr/bin/python
"""
Given three strings: s1, s2, s3, determine whether s3 is formed by the interleaving of s1 and s2.
"""
import sys

class Solution:
    """
    @params s1, s2, s3: Three strings as description.
    @return: return True if s3 is formed by the interleaving of
             s1 and s2 or False if not.
    @hint: you can use [[True] * m for i in range (n)] to allocate a n*m matrix.
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here

        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)

        if n1 + n2 != n3:
            return False

        # initialize table
        t = [[False for j in xrange(n2+1)] for i in xrange(n1+1)]

        # edges of table
        for i in xrange(n1+1):
            if s1[:i] == s3[:i]:
                t[i][0] = True

        for j in xrange(n2+1):
            if s2[:j] == s3[:j]:
                t[0][j] = True

        # bottom up
        for i in xrange(1,n1+1):
            for j in xrange(1,n2+1):

                if t[i][j-1] and s3[i+j-1] == s2[j-1]:
                    t[i][j] = True

                elif t[i-1][j] and s3[i+j-1] == s1[i-1]:
                    t[i][j] = True

                else:
                    t[i][j] = False

        return t[n1][n2]

#
if __name__ == '__main__':
    test = Solution()
    s1, s2, s3 = "aabcc", "dbbca", "aadbbcbcac"  # True
    s1, s2, s3 = "aabcc", "dbbca", "aadbbbaccc"  # False
    print test.isInterleave(s1, s2, s3)

