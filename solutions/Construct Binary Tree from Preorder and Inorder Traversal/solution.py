# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # print(preorder,inorder)
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(val=preorder[0])
        val = preorder[0]
        index = inorder.index(val)
        in_l = inorder[:index]
        in_r = inorder[index+1:]
        if len(in_l) == 0:
            pre_l = in_l
            pre_r = preorder[1:]
        else:
            index_l = preorder.index(in_l[-1])
            pre_l = preorder[1:len(in_l)+1]
            pre_r = preorder[len(in_l)+1:]
        # print(pre_l,in_l)
        # print(pre_r,in_r)
        # print("____")
        left = self.buildTree(pre_l,in_l)
        right = self.buildTree(pre_r,in_r)
        return TreeNode(val=val, left=left, right=right)