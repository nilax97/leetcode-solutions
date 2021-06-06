# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def get_leaf(root):
            if root == None:
                return []
            ans = []
            if root.left != None:
                ans += (get_leaf(root.left))
            if root.right != None:
                ans += (get_leaf(root.right))
            if root.left == None and root.right == None:
                ans = [root.val]
            return ans
        x = get_leaf(root1)
        y = get_leaf(root2)
        print(x,y)
        if len(x) != len(y):
            return False
        for i in range(len(x)):
            if x[i] != y[i]:
                return False
        return True
