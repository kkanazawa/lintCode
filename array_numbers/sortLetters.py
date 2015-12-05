#!/usr/bin/python
"""
Given a string which contains only letters. Sort it by lower case first and upper case second.

Example
For "abAcD", a reasonable answer is "acbAD"

Note
It's not necessary to keep the original order of lower-case letters and upper case letters.
"""
class Solution:
    """
    @param chars: The letters array you should sort.
    """
    def sortLetters(self, chars):
        # write your code here
        import string
        
        n = len(chars)
        i, j = 0, n-1
        while i < j:

            if chars[i] in string.lowercase:
                i += 1
            else:
                chars[i], chars[j] = chars[j], chars[i]
                j += -1
                
        return chars
        
if __name__ == '__main__':
    chars = 'abAcD'
    print Solution().sortLetters(chars)
