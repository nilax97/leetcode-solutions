class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        ans = set()
        val = [x if x.isdigit() else " " for x in word]
        val = "".join(val)
        val = val.split()
        for x in val:
            ans.add(int(x))
        return len(ans)
