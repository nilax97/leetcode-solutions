class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = dict()
        sum = 0
        start = -1
        end = -1
        value = min(1,len(s))
        while(start < len(s)-1):
            start += 1
            if s[start] in ans:
                ans[s[start]] += 1
            else:
                ans[s[start]] = 1
            while ans[s[start]] > 1:
                end += 1
                ans[s[end]] -= 1
            value = max(value,start-end)
        return value
