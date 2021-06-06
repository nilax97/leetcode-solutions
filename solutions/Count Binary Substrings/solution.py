class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        val = [0]
        if len(s) < 2:
            return 0
        prev = s[0]
        for x in s:
            if x == prev:
                val[-1] += 1
            else:
                val.append(1)
                prev = x
        for i in range(len(val)-1):
            ans += min(val[i],val[i+1])
        return ans
