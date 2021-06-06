class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def transpose(x):
            n = len(x)
            m = len(x[0])
            for i in range(n):
                for j in range(i+1,m):
                    temp = x[i][j]
                    x[i][j] = x[j][i]
                    x[j][i] = temp
        
        def reverse(x):
            n = len(x)
            m = len(x[0])
            for i in range(n):
                for j in range(m//2):
                    temp = x[i][j]
                    x[i][j] = x[i][m-j-1]
                    x[i][m-j-1] = temp
        
        transpose(matrix)
        reverse(matrix)
