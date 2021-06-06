# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        while(head != None):
            if head.val > 100000:
                return True
            head.val = 1000000
            head = head.next
        return False
