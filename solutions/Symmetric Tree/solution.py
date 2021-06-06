# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def ismirror(T1,T2):
            if(T1==None or T2==None):
                if(T1==None and T2==None):
                    return True
                else:
                    return False
            if(T1.val != T2.val):
                return False
            l = ismirror(T1.left,T2.right)
            r = ismirror(T1.right,T2.left)
            return (l and r)
        if root==None:
            return True
        else:
            return ismirror(root.left,root.right)
            
            
