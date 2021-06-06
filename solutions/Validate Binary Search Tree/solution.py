# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def preorder(root):
            if root == None:
                return []
            return preorder(root.left) + [root.val] + preorder(root.right)
        tree = preorder(root)
        for i in range(1,len(tree)):
            if tree[i] <= tree[i-1]:
                return False
        return True
