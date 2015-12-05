#!/usr/bin/python
"""
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
"""
class Solution: 
    # @param word1 & word2: Two string.
    # @return: The minimum number of steps.
    def minDistance(self, word1, word2):
        # write your code here
        n = len(word1)
        m = len(word2)

        # initialize table
        table = [ [j for j in xrange(m+1)] for i in xrange(n+1) ]

        # edges of table. they are trivial.
        for i in xrange(n+1):
            table[i][0] = i

        for j in xrange(m+1):
            table[0][j] = j

        # bottom-up approach
        for i in xrange(1,n+1):
            for j in xrange(1,m+1):

                if word1[i-1] == word2[j-1]:
                    table[i][j] = table[i-1][j-1]

                else:
                    table[i][j] = 1 + min( table[i-1][j], table[i][j-1], table[i-1][j-1] )
    
        return table[n][m]

#
if __name__ == '__main__':
    test = Solution()
    word1 = 'mart'
    word2 = 'karma'
    print test.minDistance(word1, word2)
    
