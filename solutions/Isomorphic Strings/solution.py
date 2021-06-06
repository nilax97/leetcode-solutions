class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        key1 = dict()
        key2 = dict()
        for i in range(len(s)):
            x = s[i]
            y = t[i]
            if x in key1:
                if key1[x] != y:
                    return False
            else:
                key1[x] = y
            if y in key2:
                if key2[y] != x:
                    return False
            else:
                key2[y] = x
        return True
