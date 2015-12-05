#!/usr/bin/python

"""
strstr (a.k.a find sub string), is a useful function in string operation. Your task is to implement this function.

For a given source string and a target string, you should output the first index(from 0) of target string in source string.

If target does not exist in source, just return -1.

Example
If source = "source" and target = "target", return -1.

If source = "abcdabcdefg" and target = "bcd", return 1.

Challenge
O(n2) is acceptable. Can you implement an O(n) algorithm? (hint: KMP)
"""

# 
class Solution:
    def strStr(self, source, target):
        # write your code here
        
        # detect null 
        if source is None or target is None:
            return -1
        
        # no target
        if not target:
            return 0
        
        # useful parameters
        n = len(source)
        m = len(target)
        
        # go through source and target
        for i in xrange(n-m+1):
            
            # target found in source
            if target == source[i:i+m]:
                return 1
        
        # not found
        return -1

# 
if __name__ == "__main__":
    test = Solution()

    source = "abcdabcdefg"
    target = "bcd"

    print test.strStr(source,target)


