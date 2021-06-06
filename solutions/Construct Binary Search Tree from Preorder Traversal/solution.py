# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def rectree(orderlist):
            if len(orderlist) == 0:
                return None
            if len(orderlist) == 1:
                return TreeNode(orderlist[0])
            left = list()
            right = list()
            head = TreeNode(orderlist[0])
            for i in range(1,len(orderlist)):
                if orderlist[i] < head.val:
                    left.append(orderlist[i])
                else:
                    right.append(orderlist[i])
            head.left = rectree(left)
            head.right = rectree(right)
            return head
        return rectree(preorder)
