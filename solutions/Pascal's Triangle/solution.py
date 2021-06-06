class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def fact(x):
            if x<2:
                return 1
            return int(x * fact(x-1))
        
        def comb(n, r):
            return int(fact(n)/(fact(n-r) * fact(r)))
        ans = list()
        for i in range(numRows):
            row = list()
            for j in range(i+1):
                if j>i//2:
                    row.append(row[i-j])
                else:
                    row.append(comb(i,j))
            ans.append(row)
        return ans
            
