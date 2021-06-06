# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = list()
        def check(root, level, ans):
            if root == None:
                return
            while len(ans) < level:
                ans.append(list())
            ans[level-1].append(root.val)
            check(root.left,level+1,ans)
            check(root.right, level+1,ans)
        check(root,1,ans)
        ans2 = list()
        for x in ans:
            ans2.append(x[-1])
        return ans2
