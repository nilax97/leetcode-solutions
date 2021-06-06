class Solution:
    def queryString(self, S: str, N: int) -> bool:
        for i in range(N,0,-1):
            x = bin(i).replace("0b","")
            if x not in S:
                return False
        return True
                
