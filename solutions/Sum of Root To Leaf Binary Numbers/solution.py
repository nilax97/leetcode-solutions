# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def sumparse(root, value):
            if root.left == None and root.right == None:
                return value * 2 + root.val
            left = 0
            right = 0
            if root.left != None:
                left = sumparse(root.left, value * 2 + root.val)
            if root.right != None:
                right = sumparse(root.right, value * 2 + root.val)
            return left + right
        return sumparse(root, 0)
