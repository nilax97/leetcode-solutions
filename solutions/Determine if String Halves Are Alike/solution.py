class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def checkvow(x):
            if x.lower() in ['a','e','i','o','u']:
                return True
            return False
        n = len(s)
        a = s[:n//2]
        b = s[n//2:]
        ans = 0
        for i in range(n//2):
            if checkvow(a[i]):
                ans += 1
            if checkvow(b[i]):
                ans -= 1
        if ans == 0:
            return True
        return False
