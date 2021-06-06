class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            check_r = dict()
            check_c = dict()
            check_b = dict()
            print("_____")
            for j in range(9):
                print(check_r.keys(),check_c.keys(),check_b.keys())
                r = board[i][j]
                c = board[j][i]
                b = board[3 * (i%3) + j//3][3 * (i//3) + j%3]
                if(r!="."):
                    if(r in check_r.keys()):
                        print("ROW",i,j,"-",r,check_r.keys())
                        return False
                    check_r[r] = 1
                if(c!="."):
                    if(c in check_c.keys()):
                        print("COLUMN",i,j,"-",c,check_c.keys())
                        return False
                    check_c[c] = 1
                if(b!="."):
                    if(b in check_b.keys()):
                        print("BOX",i,j,"-",b,check_b.keys())
                        return False
                    check_b[b] = 1
        return True
