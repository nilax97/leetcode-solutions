# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        def inorder(node):
            if(node==None):
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        L = inorder(root)
        for i in range(len(L)-1):
            print(L[i],p)
            if(L[i] == p.val):
                return TreeNode(L[i+1])
        return None
