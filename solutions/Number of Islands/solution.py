class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        if(n==0):
            return 0
        m = len(grid[0])
        
        def check(i,j):
            if(grid[i][j]=="0"):
                return
            grid[i][j] = "0"
            if(i>0):
                check(i-1,j)
            if(j>0):
                check(i,j-1)
            if(i < n-1):
                check(i+1,j)
            if(j < m-1):
                check(i,j+1)
            
        count = 0
        for i in range(n):
            for j in range(m):
                if(grid[i][j]=="1"):
                    count +=1
                    check(i,j)
        return count
                    
