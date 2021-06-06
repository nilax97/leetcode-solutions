class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        keys = dict()
        for w in s:
            if w in keys:
                keys[w] += 1
            else:
                keys[w] = 1
        for w in t:
            if w in keys:
                keys[w] += 1
            else:
                return w
        for k in keys.keys():
            if keys[k] % 2 != 0:
                return k
        return -1
