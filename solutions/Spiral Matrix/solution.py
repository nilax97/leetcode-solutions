class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def spiral(mat,x,y,n,m):
            ans = []
            for i in range(x,y+m):
                ans.append(mat[x][i])
            for i in range(y+1,x+n):
                ans.append(mat[i][y+m-1])
            for i in range(y+m-2,y-1,-1):
                if(n < 2):
                    break
                ans.append(mat[x+n-1][i])
            for i in range(x+n-2,x,-1):
                if (m < 2):
                    break
                ans.append(mat[i][y])
            if (n>2 and m>2):
                inter = spiral(mat,x+1,y+1,n-2,m-2)
                return ans + inter
            return ans
        return spiral(matrix,0,0,len(matrix),len(matrix[0]))
