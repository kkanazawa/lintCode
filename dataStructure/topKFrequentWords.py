#!/usr/bin/python
"""
Given a list of words and an integer k, return the top k frequent words in the list.
"""
class Solution:
    # @param {string[]} words a list of string
    # @param {int} k an integer
    # @return {string[]} a list of string
    def topKFrequentWords(self, words, k):
        # Write your code here
        from heapq import nsmallest

        n = len(words)
        d = {}
    
        for i in xrange(n):
            if words[i] in d:
                d[words[i]] += 1
            else:
                d[words[i]] = 1

        l = nsmallest(k, d.items(), key=lambda x: (-x[1],x[0]))
        return [word for word, count in l]
                     

if __name__ == '__main__':
    words = [ "yes", "lint", "code",
              "yes", "code", "baby",
              "you", "baby", "chrome",
              "safari", "lint", "code",
              "body", "lint", "code" ]
    k = 4
    words, k = ["ba","fe","bd","bf","fe","ae","ae","ed","ef","ab","cd","ac","cf","af","ed","ef","fb","ba","dc","ca","cb","ca","bc","bf","ae","ec","fa","ac","bd","af","fa","dc","cb","ed","db","fa","cb","fe","ab","bd","eb","af","ad","cd","bf","bc","cd","fd","de","fc","ef","bc","ca","fe","ac","ac","cb","eb","ca","fa","bf","ed","cb","ef","be","de","da","bc","ad","cf","ef","fd","ce","be","df","bf","fd","ef","ab","ef"], 3
    print Solution().topKFrequentWords(words, k)
        
