class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        left = [0] * (k+1)
        right = [0] * (k+1)
        for i in range(k):
            left[i+1] = left[i] + cardPoints[i]
            right[i+1] = right[i] + cardPoints[n-i-1]
        ans = 0
        right = list(reversed(right))
        for i in range(k+1):
            ans = max(ans,left[i]+right[i])
        return ans
