# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def prune(root):
            if root == None:
                return None
            root.left = prune(root.left)
            root.right = prune(root.right)
            if root.left == None and root.right == None:
                if root.val == 0:
                    return None
                else:
                    return root
            return root
        return prune(root)
