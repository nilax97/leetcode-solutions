# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next == None:
            return None
        node1 = head
        node2 = head
        count = 0
        while(node1 != None):
            node1 = node1.next
            if count > n:
                node2 = node2.next
            count += 1
        if (count == n):
            head = head.next
            return head
        node2.next = node2.next.next
        return head
