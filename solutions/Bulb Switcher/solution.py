class Solution:
    def bulbSwitch(self, n: int) -> int:
        for i in range(n+1):
            if (i+1)*(i+1) > n:
                return i
        return 0
            
