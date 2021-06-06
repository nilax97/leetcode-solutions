"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def next(node):
            if(node==None):
                return
            if(node.left == None and node.right == None):
                return
            node.left.next = node.right
            if(node.next != None):
                node.right.next = node.next.left
            next(node.left)
            next(node.right)
        
        next(root)
        
        return root
        
