from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b):
            x = int(a + b)
            y = int(b + a)
            if x < y:
                return -1
            elif x > y:
                return 1
            else:
                return 0
        b = "".join(sorted([str(x) for x in nums], reverse=True, key=cmp_to_key(compare)))
        if len(b) < 1:
            return b
        while(b[0] == '0'):
            if len(b) > 1:
                b = b[1:]
            else:
                break
        return b
