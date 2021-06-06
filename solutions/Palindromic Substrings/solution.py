class Solution:
    def countSubstrings(self, s: str) -> int:
    
        def count(s,l,h):
            ans = 0
            while(l>=0 and h < len(s)):
                if s[l] != s[h]:
                    break
                l -= 1
                h += 1
                ans += 1
            return ans
        
        ans = 0
        for i in range(len(s)):
            ans += count(s,i,i)
            ans += count(s,i,i+1)
        return ans
            
