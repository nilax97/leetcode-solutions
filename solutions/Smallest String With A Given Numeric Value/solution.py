class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = ['a'] * n
        k -= n
        index = n-1
        while(k!=0):
            if k>25:
                ans[index] = 'z'
                k -= 25
                index -= 1
            else:
                ans[index] = chr(ord('a') + k)
                break
        return "".join(ans)
        
