class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        count = collections.Counter(str(N))
        return any(count == collections.Counter(str(1 << b))
                   for b in range(31))
