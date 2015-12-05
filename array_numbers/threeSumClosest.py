#!/usr/bin/python
"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers.
"""
import sys

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target : An integer
    @return : return the sum of the three integers, the sum closest target.
    """
    # Brute-force
    # time: O(n^3)
    def threeSumClosest(self, numbers, target):
        # write your code here
        n = len(numbers)
        sum = sys.maxint
        
        for i in xrange(n):
            for j in xrange(i+1,n):
                for k in xrange(j+1,n):
                    v = numbers[i] + numbers[j] + numbers[k]
                    if abs(v-target) < sum:
                        sum = abs(v-target)
                        v_c = v
                        
        return v_c
    
    # use sort
    # time: O(n^2)
    def threeSumClosest2(self, numbers, target):
        # write your code here
        n = len(numbers)
        closest = sys.maxint
        numbers.sort()
        
        for i in xrange(n-2):
            j = i + 1
            k = n - 1

            while j < k:
                sum = numbers[i] + numbers[j] + numbers[k]
                
                if abs(sum-target) < closest:
                    closest = abs(sum-target)
                    closest_sum = sum

                if sum < target:
                    j += 1
                elif sum > target:
                    k += -1
                # target found
                else:
                    return sum
                    
        return closest_sum
        

if __name__ == '__main__':
    a, t = [-1,2,1,-4], 1  # 2
    a, t = [1,0,-1,-1,-1,-1,0,1,1,1,2], 7  # 4
    print Solution().threeSumClosest(a,t)
    print Solution().threeSumClosest2(a,t)
