# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def order(root):
            if root == None:
                return [-1]
            if root.left == None:
                return [root.val]
            if root.left.val != root.val:
                return order(root.right) + order(root.left)                
            else:
                return order(root.left) + order(root.right)
        ans = sorted(list(set(order(root))))
        if len(ans) < 2:
            return -1
        print(ans)
        return ans[1]
