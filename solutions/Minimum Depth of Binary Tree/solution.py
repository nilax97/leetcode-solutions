# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def depth(node, x):
            if node == None:
                return x-1
            if node.left == None and node.right == None:
                return x
            l = 10**5
            r = 10**5
            if node.left != None:
                l = depth(node.left,x+1)
            if node.right != None:
                r = depth(node.right,x+1)
            return min(l,r)
        return depth(root,1)
