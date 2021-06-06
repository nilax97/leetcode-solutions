"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        list1 = head
        list2 = None
        head2 = None
        val = dict()
        while(list1 != None):
            if list2 == None:
                list2 = Node(list1.val)
                head2 = list2
            else:
                list2.next = Node(list1.val)
                list2 = list2.next
            val[list1] = list2
            list1 = list1.next
        list1 = head
        list2 = head2
        while(list1 != None):
            if list1.random == None:
                list2.random = None
            else:
                list2.random = val[list1.random]
            list1 = list1.next
            list2 = list2.next
        return head2
