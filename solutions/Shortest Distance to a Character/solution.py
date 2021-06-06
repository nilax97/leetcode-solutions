class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = [-1] * len(s)
        temp = -1
        for i in range(len(s)):
            if s[i] == c:
                ans[i] = 0
                temp = i
            elif temp != -1:
                ans[i] = i - temp
        temp = -1
        for i in range(len(s)-1,-1,-1):
            if ans[i] == 0:
                temp = i
            elif temp != -1:
                if ans[i] == -1:
                    ans[i] = temp - i
                else:
                    ans[i] = min(ans[i],temp - i)
        return ans
            
