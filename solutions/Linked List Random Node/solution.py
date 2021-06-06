# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        node = head
        self.size = 0
        while(node != None):
            self.size += 1
            node = node.next
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        x = random.randint(0,self.size-1)
        node = self.head
        for i in range(x):
            node = node.next
        return node.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
