class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        path = grid.copy()
        for i in range(1,len(grid)):
            path[i][0] = path[i-1][0] + grid[i][0]
        for i in range(1,len(grid[0])):
            path[0][i] = path[0][i-1] + grid[0][i]
        for i in range(1,len(grid)):
            for j in range(1, len(grid[0])):
                path[i][j] = min(path[i][j-1],path[i-1][j]) + grid[i][j]
        return path[-1][-1]
