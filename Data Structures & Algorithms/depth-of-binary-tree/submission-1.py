# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def depth(node):
            l,r = 0,0
            if node.left:
                l = 1 + depth(node.left)
            if node.right:
                r = 1 + depth(node.right)
            return max(1, l, r)
        
        if root is None:
            return 0
        return depth(root)