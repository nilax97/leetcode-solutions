# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        n = 0
        ite = head
        while(ite != None):
            n += 1
            ite = ite.next
        ite = head
        n = n//2
        for i in range(n):
            ite = ite.next
        return ite
