# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def search(node):
            if node == None or (node.left == None and node.right == None):
                return
            
            if node.left != None:
                search(node.left)
            
            if node.right != None:
                search(node.right)
            
            temp = node.left
            node.left = node.right
            node.right = temp



        search(root)

        return root