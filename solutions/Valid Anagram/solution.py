class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        values = dict()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            x = s[i]
            y = t[i]
            if x in values:
                values[x] += 1
            else:
                values[x] = 1
            if y in values:
                values[y] -= 1
            else:
                values[y] = -1
        for x in values.keys():
            if values[x] != 0:
                return False
        return True
