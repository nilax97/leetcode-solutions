class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp, maxArea = [[0 for _1_ in range(len(matrix[0]))] for ___ in range(len(matrix))], 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                elif int(matrix[i][j]) == 1:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
                maxArea = max(maxArea, dp[i][j])
        return maxArea*maxArea
