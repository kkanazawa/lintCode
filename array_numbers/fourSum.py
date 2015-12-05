#!/usr/bin/python
"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
"""

import sys

class Solution:
    """
    @param numbersbers : Give an array numbersbersbers of n integer
    @param target : you need to find four elements that's sum of target
    @return : Find all unique quadruplets in the array which gives the sum of 
              zero.
    """
    # brute-force + hash table
    # time: O(n^3)
    def fourSum(self ,numbers, target):
        # write your code here
        n = len(numbers)
        d = dict([(j,i) for i,j in enumerate(numbers)])

        res = []
        for i in xrange(n):
            for j in xrange(i+1,n):
                for k in xrange(j+1,n):

                    ni = numbers[i]
                    nj = numbers[j]
                    nk = numbers[k]

                    idx = d.get(target - ni - nj - nk, None)

                    if idx not in [i,j,k,None]:
                        tmp = sorted([ni,nj,nk,numbers[idx]])
                        if tmp not in res:
                            res.append(tmp)
                        
        return res

    # hash table
    # time: O(n^2)
    # space: O(n^2)
    def fourSum2(self ,numbers, target):
        # write your code here
        n = len(numbers)
        res = []
        d = {}

        for i in xrange(n):
            si = numbers[i]

            for j in xrange(i+1,n):
                sj = numbers[j]

                # keys
                sum, prod = si + sj, si * sj
                
                want = target - sum

                if want in d:
                    idx = d[want].values()
                    k = len(idx)
                    for l in xrange(k):
                        idx_each = idx[l]
                        if i not in idx_each and j not in idx_each:
                            list = [si,sj] + [numbers[m] for m in idx_each]
                            list = sorted(list)
                            if list not in res:
                                res.append(list)

                if sum in d:
                    d[sum][prod] = [i,j]
                else:
                    e = {prod: [i,j]}
                    d[sum] = e

        return res

if __name__ == '__main__':
    a, t  = [1,0,-1,0,-2,2], 0
    #    a, t = [1,0,-1,-1,-1,-1,0,1,1,1,2], 2
    #    a, t = [-2,-3,5,-1,-4,5,-11,7,1,2,3,4,-7,-1,-2,-3,-4,-5], 2
    #    a, t = [1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,0,0,-2,2,-5,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99], 11

    print Solution().fourSum(a,t)
    print Solution().fourSum2(a,t)
