# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.keys = dict()
        def calcdepth(node, depth):
            if node == None:
                return depth-1
            l = calcdepth(node.left,depth+1)
            r = calcdepth(node.right,depth+1)
            
            self.keys[node.val] = max(l,r)
            return max(l,r)
        max_depth = calcdepth(root,0)
        def find_max(node):
            if node == None:
                return node
            l = -1
            r = -1
            if node.left != None:
                l = self.keys[node.left.val]
            if node.right != None:
                r = self.keys[node.right.val]
            if l == r:
                return node
            if l > r:
                return find_max(node.left)
            else:
                return find_max(node.right)
        return find_max(root)
