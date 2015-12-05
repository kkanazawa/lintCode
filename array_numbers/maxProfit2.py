#!/usr/bin/python
"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
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
            
        hold = prices[0]
        prof = 0
        
        n = len(prices)
        for i in xrange(1,n):
            if prices[i] < prices[i-1]:
                prof += prices[i-1] - hold
                hold = prices[i]
                
        return prof + prices[-1] - hold

if __name__ == '__main__':
    a = [3,2,6,5,0,3]
    print Solution().maxProfit(a)
