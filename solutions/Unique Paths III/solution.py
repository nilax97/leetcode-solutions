class Solution(object):            
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        zeros = 0
        self.fourD_walks = 0
        for i in range(m):
            for j in range(n):
                    
                if grid[i][j] == 1:
                    start = (i, j)
                
                if grid[i][j] == 0:
                    zeros +=1
                            
        self.dfs(start[0], start[1], grid, zeros+1)
        return self.fourD_walks
    
    def dfs(self, i, j , grid, zeros):  
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] == -1:
            return

        if grid[i][j] == 2:
            
            if zeros == 0:
                self.fourD_walks += 1
            return
        
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        temp = grid[i][j]
        grid[i][j] = -1
        zeros -=1
        for dir_ in dirs:
            self.dfs(i+dir_[0], j+dir_[1], grid, zeros)
        grid[i][j] = temp
