# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findpath(root,node):
            if root == None:
                return None
            if root.val == node.val:
                return [root]
            l = findpath(root.left,node)
            r = findpath(root.right,node)
            if l != None:
                return [root] + l
            if r != None:
                return [root] + r
            return None
        l = findpath(root,p)
        r = findpath(root,q)
        cur = None
        for i in range(min(len(l),len(r))):
            if l[i].val != r[i].val:
                return cur
            cur = l[i]
        return cur
        
