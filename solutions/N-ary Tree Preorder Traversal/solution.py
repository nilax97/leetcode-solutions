"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        traverse = [root]
        ans = []
        while(len(traverse) > 0):
            node = traverse.pop(0)
            if node == None:
                continue
            ans.append(node.val)
            traverse = node.children + traverse
        return ans
