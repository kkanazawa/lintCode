#!/usr/bin/python
"""
Ugly number is a number that only have factors 3, 5 and 7.

Design an algorithm to find the Kth ugly number. The first 5 ugly numbers are 3, 5, 7, 9, 15 ...
"""
class Solution:
    """
    @param k: The number k.
    @return: The kth prime number as description.
    """
    def kthPrimeNumber(self, k):
        # write your code here
        import sys
        from heapq import heappush, nsmallest

        a = []
        p, maxv = 1, sys.maxint
        while 3**p < maxv:

            for i in xrange(p+1):
                for j in xrange(p+1-i):
                    l = p - i - j
                    v = 3**i * 5**j * 7**l
                    if v < maxv:
                        heappush(a,v)

            if len(a) >= k:
                a = nsmallest(k,a)                
                maxv = a[-1]

            p += 1

        return a[-1]

if __name__ == '__main__':
    k = 10
    print Solution().kthPrimeNumber(k)
