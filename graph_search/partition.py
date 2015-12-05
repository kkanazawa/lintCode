#!/usr/bin/python
"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.
"""

import sys

class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        # write your code here
        return self.dfs(s,0)

    def dfs(self, s, idx, palin):
        res = []
        n = len(s)
        for i in xrange(idx, n):


            if self.isPalindrome(s[:i+1]):


                tmp = self.dfs(s, i+1, palin)

                res.append(tmp)

        return res


class Solution2:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        # write your code here
        res = []
        self.dfs(s, res)
        return res

    def dfs(self, s, res):
        n = len(s)
        if n == 0:
            return
            
        for i in xrange(1,n):
            if isPalindrome(s[:i]):
                tmp = []
                self.dfs(s[i:], tmp)
                if tmp:
                    for j in tmp:
                        j = [S[:i]] + j
                    res.append(j)
                else:
                    res.append([s[:i]])

    def isPalindrome(self, s):
        if not s:
            return False

        return s == s[::-1]


#
if __name__ == '__main__':
    s = 'a'
    print Solution2().partition(s)
