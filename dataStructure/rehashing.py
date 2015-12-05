#!/usr/bin/python
"""
Given the original hash table, return the new hash table after rehashing .
"""
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        # write your code here
        import sys

        n = len(hashTable)
        d = {}
        for i in xrange(n):
            node = hashTable[i]
            while node:
                v = node.val
                rem = v % (2*n)
                if rem in d:
                    d[rem].append(v)
                else:
                    d[rem] = [v]
                node = node.next


        newHash = [None for i in xrange(2*n)]
        for i in xrange(2*n):
            if i not in d:
                continue
            l = d[i][::-1]
            m = len(l)
            head = None
            for j in xrange(m):
                head = ListNode(l[j], head)
            newHash[i] = head

        return newHash

if __name__ == '__main__':
    n1 = ListNode(9, None)
    n2 = ListNode(21, n1)
    n3 = ListNode(14, None)
    ht = [None, n2, n3, None]
                  
    list = Solution().rehashing(ht)
    for i in xrange(len(list)):
        node = list[i]
        print 'i =',i
        while node:
            print node.val
            node = node.next
