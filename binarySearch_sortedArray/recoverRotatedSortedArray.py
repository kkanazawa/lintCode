#!/usr/bin/python
"""
Given a rotated sorted array, recover it to sorted array in-place.
"""
class Solution:
    """
    @param nums: The rotated sorted array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here

        idx = self.f(nums)
        nums.extend(nums[:idx])
        del nums[:idx]
        print nums

    def f(self,A):
    
        mid = len(A)/2

        # base case
        if len(A) <= 1:
            return 0
            
        # recursion
        elif A[0] == A[-1]:
            return 1 + self.f(A[1:-1])

        
        elif A[0] > A[mid]:
            A_sub = A[1:mid+1]  # mid+1: mid might be the first element
            return 1 + self.f(A_sub)  # note A[0] removed

        elif A[mid] > A[-1]:
            A_sub = A[mid+1:]
            return mid + 1 + self.f(A_sub)  # note mid+1 elements removed
        
        # no rotation    
        else: 
            return 0

#
if __name__ == "__main__":
    test = Solution()
    nums = [4,5,1,2,3]
    test.recoverRotatedSortedArray(nums)
