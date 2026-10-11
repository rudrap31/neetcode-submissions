# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:


        cnt = [k]
        res = [root.val]
        def traverse(node):
            if not node:
                return
            
            traverse(node.left)
            if cnt[0] == 0:
                return
            cnt[0] -= 1
            if cnt[0] == 0:
                res[0] = node.val
                return
            traverse(node.right)

        
        traverse(root)
        return res[0]
        