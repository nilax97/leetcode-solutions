# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self, node, height):
        if node == None:
            return
        if len(self.mat) < height:
            self.mat.append([])
        self.mat[height-1].append(node.val)
        self.dfs(node.left,height+1)
        self.dfs(node.right,height+1)
        
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.mat = list()
        self.dfs(root,1)
        ans = 0
        for x in self.mat[-1]:
            ans += x
        return ans
        
