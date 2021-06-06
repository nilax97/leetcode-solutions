class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        s = '_' + s
        n, nxt = len(s), [{} for _ in s]
        for i, c in enumerate(s):
            for j in range(i-1, -1, -1):
                nxt[j][c] = i
                if s[j] == c: break

        def find(word):
            i = 0
            for c in word:
                i = nxt[i].get(c)
                if i is None: return False
            return True
        res = ""
        for word in d:
            if find(word) and (not res or (-len(word), word) < (-len(res), res)):
                res = word
        return res
