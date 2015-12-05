#!/usr/bin/python

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates2(self, head):
        # write your code here
        if not head:
            return None
        
        dummy = ListNode(0, head)
        # two pointers
        slow = dummy
        fast = head
        
        while fast is not None and fast.next is not None:
            
            if fast.val == fast.next.val:
                # put fast on last element
                while fast.next is not None and fast.val == fast.next.val:
                    fast = fast.next
                slow.next = fast.next
                fast = fast.next
                
            else:
                slow = slow.next
                fast = fast.next
            
        return dummy.next
            

if __name__ == '__main__':

    a = [0, 1, 1, 2, 3, 3]

    head = None
    for i in a[::-1]:
        head = ListNode(i, head)

    before = []
    node = head
    while node is not None:
        before.append(node.val)
        node = node.next
    print before

    #
    after = []
    test = Solution()
    node = test.deleteDuplicates2(head)
    while node is not None:
        after.append(node.val)
        node = node.next
    print after
    
