# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        def addrow(root,n,v,d):
            if root == None:
                return None
            if n > (d-1):
                return root
            if n < (d-1):
                left = addrow(root.left,n+1,v,d)
                right = addrow(root.right,n+1,v,d)
                root.left = left
                root.right = right
                return root
            else:
                left = root.left
                right = root.right
                root.left = TreeNode(val=v, left=left)
                root.right = TreeNode(val=v,right=right)
                return root
        if (d==1):
            return TreeNode(val=v,left=root)
        return addrow(root,1,v,d)
