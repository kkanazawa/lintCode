#!/usr/bin/python
"""
Given a singly linked list L: L0 -> L1 -> ... -> Ln-1 -> Ln,
reorder it to: L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...

You must do this in-place without altering the nodes' values.
"""

import sys

def main():
    
    # create a linked list for test
    a = [1,2,3,4,5,6]
    head = None
    for val in a[::-1]:
        head = ListNode(val, head)

    # check
    before = []
    node = head
    while node:
        before.append(node.val)
        node = node.next
    print before

    # test the algorithm
    test = Solution()
    head = test.reorderList(head)

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
    @return: nothing
    """
    def reorderList(self, head):
        # write your code here
        if not head or not head.next:
            return head

        # split list into {head, head2}
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        head2 = slow.next
        slow.next = None

        # reverse head2
        head2 = self.reverse(head2)

        # merge {head, head2}
        node, node2 = head, head2
        while node and node2:
            tmp, tmp2 = node.next, node2.next

            node.next = node2
            node2.next = tmp
            
            node, node2 = tmp, tmp2

        return head
        
    def reverse(self, head):
        # write your code here
        if not head or not head.next:
            return head
        
        node = head.next
        head.next = None
        
        while node:
            tmp = node.next
            node.next = head
            head = node
            node = tmp
            
        return head
           

if __name__ == '__main__':
    main()
