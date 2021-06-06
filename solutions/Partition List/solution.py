# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        ans = []
        node = head
        while(node != None):
            ans.append(node.val)
            node = node.next
        ans1 = []
        ans2 = []
        for val in ans:
            if val < x:
                ans1.append(val)
            else:
                ans2.append(val)
        ans = ans1 + ans2
        node = head
        index = 0
        while( node != None):
            node.val = ans[index]
            node = node.next
            index += 1
        return head
