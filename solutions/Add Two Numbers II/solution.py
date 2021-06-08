# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        v1 = 0
        v2 = 0
        while(l1 != None):
            v1 = v1 * 10
            v1 += l1.val
            l1 = l1.next
        while(l2 != None):
            v2 = v2 * 10
            v2 += l2.val
            l2 = l2.next
        ans = [int(i) for i in str(v1 + v2)]
        val = ListNode(ans[0])
        node = val
        for i in range(1,len(ans)):
            node.next = ListNode(ans[i])
            node = node.next
        return val
        
            
