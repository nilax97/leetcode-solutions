class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        return X - Y if X >= Y else 1 + Y % 2 + self.brokenCalc(X, (Y + 1) // 2)
