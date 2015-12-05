#!/usr/bin/python
"""
Reverse a linked list.
"""

def main():

    # create a linked list 
    a = [1,2,3]
    head1 = getLinkedList(a)
    head2 = getLinkedList(a)

    # check
    print toList(head1)

    # reverse
    test = Solution()

    head1 = test.reverse(head1)
    print toList(head1)

    head2 = test.reverse2(head2)
    print toList(head2)

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
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list. 
                  Reverse it in-place.
    """
    # first attempt
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

    # better 
    def reverse2(self, head):
        # write your code here

        dummy = ListNode(0, None)
        
        while head:
            tmp = head.next
            head.next = dummy.next
            dummy.next = head
            head = tmp
            
        return dummy.next
            
if __name__ == '__main__':
    main()
