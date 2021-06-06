class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        cmax = 0
        for i in range(len(A) - 2):
            cmax = max(cmax, A[i])
            if cmax > A[i + 2]:
                return False
        return True
