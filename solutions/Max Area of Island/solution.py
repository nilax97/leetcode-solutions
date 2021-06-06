class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def grow(grid,i,j):
            ans = 0
            check = []
            check.append([i,j])
            while(len(check) > 0):
                x = check.pop(0)
                if grid[x[0]][x[1]] == 0:
                    continue
                ans += 1
                grid[x[0]][x[1]] = 0
                if x[0] > 0:
                    check.append([x[0]-1,x[1]])
                if x[0] < (len(grid) - 1):
                    check.append([x[0]+1,x[1]])
                if x[1] > 0:
                    check.append([x[0],x[1]-1])
                if x[1] < (len(grid[0]) - 1):
                    check.append([x[0],x[1]+1])
            return ans
            
        ans = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans = max(ans,grow(grid,i,j))
        return ans
