class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        total = 0
        for x in shift:
            if x[0] == 0:
                direction = 1
            else:
                direction = -1
            total = total + direction * x[1]
        total = total%len(s)
        s = s[total:] + s[:total]
        return s
