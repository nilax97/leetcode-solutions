class Solution:
    def toLowerCase(self, s: str) -> str:
        diff = ord('a') - ord('A')
        ulim = ord('Z') + 1
        llim = ord('A') - 1
        ans = []
        for x in s:
            t = ord(x)
            if t < ulim and t > llim:
                ans.append(chr(t + diff))
            else:
                ans.append(x)
        return "".join(ans)
