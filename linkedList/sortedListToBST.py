#!/usr/bin/python
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST(self, head):
        # write your code here
        if not head:
            return None
        if head.next is None:
            return TreeNode(head.val)
        
        dummy = ListNode(0, head)
        
        mid = self.getMidNode(dummy)

        root = TreeNode(mid.next.val)
        
        # right child
        root.right = self.sortedListToBST(mid.next.next)
        
        # left child
        if mid == dummy:
            root.left = None
        else:
            mid.next = None
            root.left = self.sortedListToBST(head)

        return root
    
    # 
    def getMidNode(self, head):
        slow = head
        fast = head.next
        
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        return slow
