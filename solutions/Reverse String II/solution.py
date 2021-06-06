class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = []
        count = 0
        while(True):
            start = count * k
            end = min((count + 1) * k,len(s))
            if start >= len(s):
                break
            if count % 2 == 0:
                ans.append(s[start:end][::-1])
            else:
                ans.append(s[start:end])
            count += 1
        return "".join(ans)
            
