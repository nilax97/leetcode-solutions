# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def path_sum(node,path,value):
            global ans
            if(node==None):
                return 0
            path.append(node.val)
            l = path_sum(node.left,path,value)
            r = path_sum(node.right,path,value)
            
            count = 0
            ans = 0
            for i in range(len(path)-1,-1,-1):
                count += path[i]
                if(count==value):
                    ans += 1
            print(node.val,ans + l + r)
            path.pop(-1)
            return ans + l + r
        return path_sum(root,[],sum)

