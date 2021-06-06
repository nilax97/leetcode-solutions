# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = list()
        def fill(node, level):
            if node == None:
                return
            if len(ans) < (level+1):
                ans.append(list())
            ans[level].append(node.val)
            fill(node.left,level+1)
            fill(node.right,level+1)
        fill(root,0)
        return ans
