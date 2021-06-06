# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        check = list()
        check.append(original)
        check2 = list()
        check2.append(cloned)
        while len(check) > 0:
            node = check.pop(0)
            node2 = check2.pop(0)
            if node.val == target.val:
                return node2
            if node.left != None:
                check.append(node.left)
                check2.append(node2.left)
            if node.right != None:
                check.append(node.right)
                check2.append(node2.right)
        return None
