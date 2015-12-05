#!/usr/bin/python
"""
Sort a linked list in O(n log n) time using constant space complexity.
"""

import sys
from heapq import heappush, heappop

def main():
    a = [3,2,1]
    head = None
    for i in a[::-1]:
        head = ListNode(i,head)
        
    # check
    before = []
    node = head
    while node:
        before.append(node.val)
        node = node.next
    print before

    # sort
    test = Solution()
    head = test.sortList(head)

    # result
    after = []
    node = head
    while node:
        after.append(node.val)
        node = node.next
    print after

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """
    def sortList(self, head):
        # write your code here
        
        if not head or not head.next:
            return head
        
        h = []
        node = head
        while node:
            heappush(h, (node.val, node))
            node = node.next
            
        head = h[0][1]
        node = heappop(h)[1]
        while h:
            node.next = heappop(h)[1]
            node = node.next

        node.next = None

        return head
        
if __name__ == '__main__':
    main()
