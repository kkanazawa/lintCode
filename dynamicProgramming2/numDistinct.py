#!/usr/bin/python
"""
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
"""
class Solution: 
    # @param S, T: Two string.
    # @return: Count the number of distinct subsequences
    def numDistinct(self, S, T):
        # write your code here
        n = len(S)
        m = len(T)

        # trivial case
        if S == T:
            return 1
        if not T or n < m:
            return 0

        # initialize table 
        table = [ [0 for j in xrange(m+1)] for i in xrange(n+1) ]

        # bottom-up
        for i in xrange(n+1):
            table[i][0] = 1  # trivial case

            for j in xrange(1,m+1):
    
                if S[i-1]==T[j-1]:
                    table[i][j] = table[i-1][j-1] + table[i-1][j]

                else:
                    table[i][j] = table[i-1][j]

        return table[n][m]     


# test
if __name__=='__main__':
    test = Solution()
    S = 'rabbbit'
    T = 'rabbit'
    print test.numDistinct(S,T)
    
