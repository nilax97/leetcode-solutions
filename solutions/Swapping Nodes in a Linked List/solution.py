# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        n = 1
        ans = list()
        node = head
        while(node != None):
            ans.append(node.val)
            node = node.next
        n = len(ans)
        print(ans)
        temp = ans[k-1]
        ans[k-1] = ans[n-k]
        ans[n-k] = temp
        print(ans)
        node = head
        for i in range(n):
            node.val = ans[i]
            node = node.next
        return head
