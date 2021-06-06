# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if(head==None or head.next==None):
            return head
        odd = head
        even = head.next
        even_head = even
        while(odd.next!=None and even.next!=None):
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next=even_head
        return head
