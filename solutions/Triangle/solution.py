class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(row + 1):
                triangle[row][col] += min(triangle[row + 1][col], 
                                          triangle[row + 1][col + 1])
        return triangle[0][0]
