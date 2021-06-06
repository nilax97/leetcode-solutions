class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if len(A) == 0:
            return True
        for i in range(len(A)):
            if A[i:] + A[:i] == B:
                return True
        return False
