#!/usr/bin/python
"""
Merge k sorted linked lists and return it as one sorted list.

Analyze and describe its complexity.
"""

import heapq as hq
import sys

def main():
    
    a = [2, 4]
    head = None
    for i in a[::-1]:
        head = ListNode(i, head)

    head2 = None
    head3 = ListNode(-1)
    lists = [head, head2, head3]

    # check
    before = []
    for node in lists:
        b = []
        while node is not None:
            b.append(node.val)
            node = node.next
        before.append(b)
    print before

    # test
    after = []
    test = Solution()
    node = test.mergeKLists(lists)

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
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here

        a = []

        for node in lists:
            while node:
                hq.heappush(a, node.val)
                node = node.next

        dummy = ListNode(0)
        node = dummy

        while len(a) > 0:
            node.next = ListNode(hq.heappop(a))
            node = node.next

        return dummy.next

#
if __name__ == '__main__':
    main()
    
    


