#!/usr/bin/python
"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
"""
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if not prices:
            return 0

        import sys
        buy, sell, prof = sys.maxint, - sys.maxint, - sys.maxint
        n = len(prices)
        
        for i in xrange(n):
            a = prices[i]
            if a < buy:
                buy, sell = a, a
            sell = max(sell, a)
            prof = max(prof, sell - buy)
            
        return prof

if __name__ == '__main__':
    a = [3,2,3,1,2]  # 1
    print Solution().maxProfit(a)
