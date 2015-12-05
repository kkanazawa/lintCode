#!/usr/bin/python
"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
"""
class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    # brute force
    def largestRectangleArea(self, height):
        # write your code here
        n = len(height)
        area = 0
        for i in xrange(n):
            for j in xrange(i,n):
                this_area = (j-i+1) * min(height[i:j+1])
                area = max(area, this_area)
                
        return area

    # time: O(n^2), worst
    # space: O(n)
    def largestRectangleArea2(self, height):
        # write your code here
        s = [-1]
        height.append(-1)
        n = len(height)
        area = 0

        for i in xrange(n):

            # calculate 
            while height[i] < height[s[-1]]:
                tmp = s.pop()
                area = max(area, height[tmp]*(i-s[-1]-1))
                
            s.append(i)

        return area

if __name__ == '__main__':
    a = [2,1,5,6,2,3]
    a = [1,1]
    print Solution().largestRectangleArea(a)
    print Solution().largestRectangleArea2(a)
