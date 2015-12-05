#!/usr/bin/python
"""
Given two sorted integer arrays A and B, merge B into A as one sorted array.
"""

class Solution:
    """
    @param A: sorted integer array A which has m elements, 
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        
        i = m-1
        j = n-1
        # 
        while i >= 0 and j >= 0:
            #
            if A[i] > B[j]:
                A[i+j+1] = A[i]
                i -= 1
            
            else:
                A[i+j+1] = B[j]
                j -= 1
        
        # A is finished
        if i < 0: 
            A[:i+j+2] = B[:j+1]

        return A
            
#
if __name__ == "__main__":
    test = Solution()
    
    A = [1, 2, 3, 0, 0]
    B = [4, 5]

    print test.mergeSortedArray(A, 3, B, 2)
