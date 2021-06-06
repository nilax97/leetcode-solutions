# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        node = head
        n = 0
        ans = []
        while(node != None):
            n += 1
            ans.append(node.val)
            node = node.next
        for i in range(n//2):
            if ans[i] != ans[n - i - 1]:
                return False
        return True
        
