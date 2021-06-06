# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ans = list()
        for node in lists:
            val = node
            while (val != None):
                ans.append(val.val)
                val = val.next
        ans = sorted(ans)
        sub = None
        point = None
        for x in ans:
            if sub == None:
                sub = ListNode(x)
                point = sub
            else:
                point.next = ListNode(x)
                point = point.next
        return sub
        # home = None
        # point = None
        # val = None
        # while True:
        #     val = None
        #     for i in range(len(lists)):
        #         if lists[i] == None:
        #             continue
        #         if val == None:
        #             val = i
        #             continue
        #         if lists[i].val < lists[val].val:
        #             val = i
        #     if val == None:
        #         break
        #     if home == None:
        #         home = lists[val]
        #         point = home
        #         lists[val] = lists[val].next
        #     else:
        #         point.next = lists[val]
        #         point = point.next
        #         lists[val] = lists[val].next
        # return home
            
