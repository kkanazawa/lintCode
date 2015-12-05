#!/usr/bin/python

"""
Given a list of numbers that may has duplicate numbers, return all possible subsets
"""
class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, S):
        # write your code here
        import copy
        S.sort()
        
        # base case
        if not S:
            return [S]

        # recursion
        else:
            x = S[0]
            S_sub = S[1:]
            list = self.subsetsWithDup(S_sub)
            list = list + copy.deepcopy(list)

            for j in xrange(len(list)/2):
                list[j].insert(0,x)
                
            list2 = []
            for k in list:
                if k not in list2:
                    list2.append(k)

            return list2
            
if __name__ == "__main__":
    test = Solution()
    S = [1,2,2]
    print test.subsetsWithDup(S)
