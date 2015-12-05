#!/usr/bin/python
"""
Given a binary tree, find the maximum path sum from root.

The path may end at any node in the tree.
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root the root of binary tree.
    @return an integer
    """
    def maxPathSum2(self, root):
        # Write your code here
        if not root:
            return root
        
        if root.left:
            left = self.maxPathSum2(root.left)
        else:
            left = 0
            
        if root.right:
            right = self.maxPathSum2(root.right)
        else:
            right = 0
            
        left = max(left, 0)
        right = max(right, 0)
        
        return root.val + max(left, right)
        
if __name__ == '__main__':
    root = TreeNode(1)
    root.left, root.right = TreeNode(2), TreeNode(-3)

    print Solution().maxPathSum2(root)
