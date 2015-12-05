#!/usr/bin/python
"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2->null and x = 3,
return 1->2->2->4->3->5->null.
"""
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of linked list.
    @param x: an integer
    @return: a ListNode 
    """
    def partition(self, head, x):
        # write your code here
        
        if not head:
            return None
    
        leftDummy = ListNode(0)  # < x
        rightDummy = ListNode(0)  # >= x

        # 2 pointers
        left = leftDummy
        right = rightDummy

        node = head
        while node is not None:

            # add node to left
            if node.val < x: 
                left.next = node
                left = left.next

            # add node to right
            else:  
                right.next = node
                right = right.next

            node = node.next

        # concatenate left and right
        right.next = None
        left.next = rightDummy.next

        return leftDummy.next    

# 
if __name__ == '__main__':

    # input
    a = [1, 4, 3, 2, 5, 2]
    x = 3

    # linked list
    head = None
    for i in a[::-1]:
        head = ListNode(i, head)

    # check
    before = []
    node = head
    while node is not None:
        before.append(node.val)
        node = node.next
    print x, before

    # test
    after = []
    test = Solution()
    node = test.partition(head, x)
    while node is not None:
        after.append(node.val)
        node = node.next
    print x, after

    


