# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def depth(node):
            if(node == None):
                return 0
            l = depth(node.left)
            r = depth(node.right)
            return max(l,r) +1
        return depth(root)
