#!/usr/bin/python

"""
Given a set of distinct integers, return all possible subsets.

"""

class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
        # write your code here
        
        import copy
        S.sort()
        
        # base case (null list)
        if not S:
            return [S]

        else:
            x = S[0]
            sub = self.subsets(S[1:])
            n = len(sub) 
        
            # duplicate sub and add to original one
            sub = sub + copy.deepcopy(sub)

            #   
            for i in xrange(n):
                sub[i].insert(0,x)
                
            return sub

#
if __name__ == "__main__":

    test = Solution()
    S = [i for i in xrange(3)]

    print test.subsets(S)
