# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def inorder(root):
            if root == None:
                return "-"
            return str(root.val)+","+inorder(root.left)+","+inorder(root.right)
        if inorder(p) == inorder(q):
            return True
        return False
