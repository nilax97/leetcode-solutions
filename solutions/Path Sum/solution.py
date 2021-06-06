# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def path(node,value):
            if(node==None):
                return False
            if node.left==None and node.right==None:
                if value == node.val:
                    return True
                else:
                    return False
                
            if(path(node.left,value-node.val) or path(node.right,value-node.val)):
                return True
            else:
                return False
        if(root==None):
            return False
        return path(root,sum)
