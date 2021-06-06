# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(node):
            if(node==None):
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        L = inorder(root)
        return L[k-1]
