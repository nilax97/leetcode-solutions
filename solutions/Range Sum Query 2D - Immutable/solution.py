class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = list()
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            self.matrix.append(list())
            for j in range(m):
                self.matrix[i].append(0)
                if i==0 and j==0:
                    self.matrix[0][0] = matrix[0][0]
                elif i==0:
                    self.matrix[0][j] = matrix[0][j] + self.matrix[0][j-1]
                elif j == 0:
                    self.matrix[i][0] = matrix[i][0] + self.matrix[i-1][0]
                else:
                    self.matrix[i][j] = self.matrix[i-1][j] + self.matrix[i][j-1] - self.matrix[i-1][j-1] + matrix[i][j]
        # for i in range(n):
        #     print(matrix[i])
        # print("____")
        # for i in range(n):
        #     print(self.matrix[i])
        # print("____")
                
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        ans += self.matrix[row2][col2]
        if row1 != 0:
            ans -= self.matrix[row1-1][col2]
        if col1 != 0:
            ans -= self.matrix[row2][col1-1]
        if col1 != 0 and row1 != 0:
            ans += self.matrix[row1-1][col1-1]
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
