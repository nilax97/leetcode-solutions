class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        ans = set()
        for i in range(len(s) - k + 1):
            ans.add(s[i:i+k])
        if len(ans) < 2**k:
            return False
        return True
