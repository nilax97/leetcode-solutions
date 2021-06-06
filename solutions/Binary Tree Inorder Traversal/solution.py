# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = list()
        stack = list()
        stack.append(root)
        while(len(stack)>0):
            x = stack.pop(-1)
            if(x==None):
                break
            if(x.left == None and x.right == None):
                ans.append(x.val)
                continue
            if(x.right != None):
                stack.append(x.right)
            stack.append(TreeNode(x.val))
            if(x.left != None):
                stack.append(x.left)
        return ans
