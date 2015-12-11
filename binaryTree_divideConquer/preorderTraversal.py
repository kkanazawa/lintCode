#!/usr/bin/python
"""
Given a binary tree, return the preorder traversal of its nodes' values.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """
    def __init__(self):
        self.a = []
    
    def preorderTraversal(self, root):
        # write your code here
        if not root:
            return self.a
        
        self.a.append(root.val)
        
        if root.left:
            self.preorderTraversal(root.left)
            
        if root.right:
            self.preorderTraversal(root.right)
            
        return self.a

def main():

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print Solution().preorderTraversal(root)

if __name__ == '__main__':
    main()
