# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def preorder(node):
            if node == None:
                return None
            preorder(node.left)
            preorder(node.right)
            left = node.left
            right = node.right
            node.left = None
            node.right = left
            if node.right == None:
                node.right = right
                return
            root = node.right
            while(root.right != None):
                root = root.right
            root.right = right
        preorder(root)        
                
            
