#!/usr/bin/python
"""
Given n items with size Ai and value Vi, and a backpack with size m. What's the maximum value can you put into the backpack?
"""
class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A & V: Given n items with size A[i] and value V[i]
    # @return: The maximum value
    def backPackII(self, m, A, V):
        # write your code here
                                
        # include all items
        if sum(A) <= m:  
            return sum(V)

        n = len(A)
        
        # 1-D table (space complexity: O(m))
        dp = [0 for j in xrange(m+1)]

        # bottom up
        for i in xrange(1,n+1):

            j = m  # capacity of backpack
            item_size = A[i-1]
            item_val = V[i-1]

            while j >= item_size: 
                # update
                dp[j] = max( dp[j], dp[j-item_size] + item_val ) 
                    
                j -= 1

        return dp[m]

#
if __name__ == '__main__':
    test = Solution()
    A = [2,3,5,7]
    V = [1,5,2,4]
    m = 10
    print test.backPackII(m, A, V)
