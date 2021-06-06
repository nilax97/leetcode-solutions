class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        carry = 0
        n = len(A)
        for i in range(n-1,-1,-1):
            A[i] += carry + K % 10
            K = K // 10
            carry = A[i] // 10
            A[i] = A[i] % 10
        while(K != 0):
            A = [K % 10 + carry] + A
            K = K // 10
            carry = A[0] // 10
            A[0] = A[0] % 10
        if carry != 0:
            A = [carry] + A
        return A
