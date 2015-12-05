#!/usr/bin/python
"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume NO duplicates in the array.
"""
class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        # write your code here

        # useful parameters
        low = 0
        high = len(A) - 1

        if not A:
            return 0
        
        # binary search
        while (low + 1 <= high):

            mid = (low + high) / 2

            if A[mid] < target:
                low = mid + 1
            else:
                high = mid

        if A[low]>=target:
            return low
            
        # target > A[-1]
        else:  
            return low + 1

#
if __name__ == "__main__":
    test = Solution()

    A = [1,3,5,6]
    target = 5

    print test.searchInsert(A, target)
