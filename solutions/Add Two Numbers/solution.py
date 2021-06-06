# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode()
        head = ans
        carry = 0
        while l1 != None or l2 != None:
            temp = carry
            if l1 != None:
                temp += l1.val
                l1 = l1.next
            if l2 != None:
                temp += l2.val
                l2 = l2.next
            ans.val = temp % 10
            carry = temp // 10
            if l1 == None and l2 == None:
                if carry == 0:
                    continue
                else:
                    ans.next = ListNode(carry)
                    ans = ans.next
                    continue
            ans.next = ListNode()
            ans = ans.next
        return head
                
