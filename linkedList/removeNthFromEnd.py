#!/usr/bin/python
"""
Given a linked list, remove the nth node from the end of list and return its head.
"""
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        
        if not head or n == 0:
            return None
        
        # fast and slow pointers
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        
        # move fast n steps
        for i in xrange(n):
            fast = fast.next

        # fast arrives at last node
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        
        return dummy.next

#
if __name__ == '__main__':

    # linked list
    node5 = ListNode(5, None)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    head = ListNode(1, node2)

    n = 2

    # check
    before = []
    node = head
    while node is not None:
        before.append(node.val)
        node = node.next
    print before

    # remove Nth element
    after = []
    test = Solution()
    head = test.removeNthFromEnd(head, n)
    while head is not None:
        after.append(head.val)
        head = head.next
    print after


    

