# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        val = []
        node = head
        while(node != None):
            val.append(node.val)
            node = node.next
        def listtonode(x):
            if len(x) == 0:
                return None
            mid = len(x) // 2
            left = listtonode(x[:mid])
            right = listtonode(x[mid+1:])
            node = TreeNode(val=x[mid],left=left,right=right)
            return node
        return listtonode(val)
            
