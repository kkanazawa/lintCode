#!/usr/bin/python
"""
Given an array of n objects with k different colors (numbered from 1 to k), sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.
"""

import sys

class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    # space: O(k)
    def sortColors2(self, colors, k):
        # write your code here
        n = len(colors)
        count = [0 for j in xrange(k)]

        for i in xrange(n):
            count[ colors[i] - 1 ] += 1

        i = 0
        for j in xrange(k):
            while count[j] > 0:
                colors[i] = j + 1 
                count[j] += -1
                i += 1

        return colors

if __name__ == '__main__':
    a = [3,2,2,1,4]
    k = 4
    print Solution().sortColors2(a,k)
