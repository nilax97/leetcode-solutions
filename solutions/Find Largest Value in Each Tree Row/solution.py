# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        val = list()
        def check(root,level,ans):
            if root == None:
                return
            while level > len(ans):
                ans.append(-2**31)
            ans[level-1] = max(ans[level-1],root.val)
            check(root.left,level+1,ans)
            check(root.right,level+1,ans)
        check(root,1,val)
        return val
                
            
