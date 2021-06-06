# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def diameter_calc(root: TreeNode) -> (int,int):
            if root == None:
                return (0,0)
            if root.left == None and root.right == None:
                return (0,1)
            a1 = 0
            b1 = 0
            a2 = 0
            b2 = 0
            if(root.left != None):
                (a1,b1) = diameter_calc(root.left)
            if(root.right != None):
                (a2,b2) = diameter_calc(root.right)
            b = max(b1,b2) + 1
            a = max(max(a1,a2),b1+b2)
            return (a,b)
        (a,b) = diameter_calc(root)
        return a
            
