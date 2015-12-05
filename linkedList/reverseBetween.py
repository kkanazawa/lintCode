#!/usr/bin/python
"""
Reverse a linked list from position m to n.
"""

import sys

def main():

    # create a linked list 

    a = [1,2,3,4,5]
    head = getLinkedList(a)

    # check
    print toList(head)

    # reverse
    test = Solution()
    m, n = 1, 4
    head = test.reverseBetween(head,m,n)

    print toList(head)
    

def getLinkedList(a):
    head = None
    for i in a[::-1]:
        head = ListNode(i,head)
    return head

def toList(head):
    a = []
    node = head
    while node:
        a.append(node.val)
        node = node.next
    return a

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The head of linked list
    @param m: start position
    @param n: end position
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dum2 = ListNode(0, head)  # necessary for n=1

        # find m-th node
        prev = dum2
        for i in xrange(m-1):
            prev = prev.next
        node = prev.next

        # same as reverse.py
        for i in xrange(n-m+1):
            tmp = node.next
            node.next = dummy.next
            dummy.next = node
            node = tmp

        # concatenate LLs
        prev.next.next = node
        prev.next = dummy.next

        return dum2.next


if __name__ == '__main__':
    main()
