# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        values = dict()
        def check(root):
            if root==None:
                return
            x = root.val
            if x in values:
                values[x] += 1
            else:
                values[x] = 1
            if root.left !=None:
                check(root.left)
            if root.right !=None:
                check(root.right)
        check(root1)
        check(root2)
        ans = list()
        for key in sorted(values.keys()):
            if values[key] == 1:
                ans.append(key)  
            else:
                ans.append(key)
                ans.append(key)
        return ans
            
            
