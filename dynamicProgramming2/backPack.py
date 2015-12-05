#!/usr/bin/python
"""
Given n items with size Ai, an integer m denotes the size of a backpack. How full you can fill this backpack?
"""
class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backPack(self, m, A):
        # write your code here
                
        # put one item
        if m in A:
            return m
        
        # include all items
        if sum(A) <= m:  
            return sum(A)

        n = len(A)
        
        # 1-D table (space complexity: O(m))
        dp = [0 for j in xrange(m+1)]

        # bottom up
        for i in xrange(1,n+1):

            j = m  # capacity of backpack
            item_size = A[i-1]
            
            while j >= item_size: 
                # update
                dp[j] = max( dp[j], dp[j-item_size] + item_size ) 

                # backpack fulfilled
                if dp[j] == m:
                    return m
                    
                j -= 1

        return dp[m]

#
if __name__ == '__main__':
    test = Solution()
    A = [2,3,5,7]
    m = 11
    print test.backPack(m, A)
