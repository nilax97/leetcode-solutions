class Solution {
    public int maxIncreaseKeepingSkyline(int[][] grid) {
        int x = grid.length;
        int y = grid[0].length;
        int[] xmax = new int[x];
        int[] ymax = new int[y];
        for(int i=0; i<x; ++i)
        {
            for(int j=0; j<y; ++j)
            {
                if(grid[i][j]>xmax[i])
                {
                    xmax[i] = grid[i][j];
                }
                if(grid[i][j]>ymax[j])
                {
                    ymax[j] = grid[i][j];
                }
            }
        }
        int total = 0;
        for(int i=0; i<x; ++i)
        {
            for(int j=0; j<y; ++j)
            {
                int t =  Math.min(xmax[i],ymax[j]);
                if(grid[i][j]<t)
                {
                    total += (t - grid[i][j]);
                    grid[i][j] = t;
                }
            }
        }
        return total;
    }
}
