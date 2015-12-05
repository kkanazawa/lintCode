#!/usr/bin/python
"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        # write your code here

        if head is None:
            return None

        node = head
        while node.next is not None:

            # found duplicate
            if node.val == node.next.val:
                node.next = node.next.next

            else:
                node = node.next

        return head

#
if __name__ == '__main__':
    
    # linked list
    a = [1, 1, 2]
    head = None
    for i in a[::-1]:
        head = ListNode(i, head)

    # check
    before = []
    node = head
    while node is not None:
        before.append(node.val)
        node = node.next
    print before

    # test
    after = []
    test = Solution()
    node = test.deleteDuplicates(head)
    while node is not None:
        after.append(node.val)
        node = node.next
    print after
    
