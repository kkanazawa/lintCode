#!/usr/bin/python
"""

"""
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        n = len(prices)
        if (n<2):
            return 0
        st = prices[0]
        mp=[]
        mprof = 0
        for i in range(0,n):
            if (prices[i]-st>mprof):
                mprof = prices[i]-st
            if (prices[i]<st):
                st = prices[i]
            mp.append(mprof)
         
        mprof = 0
        ed = prices[-1]
        for i in range(n-2,-1,-1):
            if (ed - prices[i] + mp[i] > mprof):
                mprof = ed - prices[i] + mp[i]
            if (prices[i]>ed):
                ed = prices[i]
        return mprof
                 
if __name__ == '__main__':
    a = [2,5,8]
    print Solution().maxProfit(a)
