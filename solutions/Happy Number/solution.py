class Solution:
    def isHappy(self, n: int) -> bool:
        check = dict()
        check[n] = 1
        while(n!=1):
            temp = 0
            while(n>0):
                temp = temp + (n%10)*(n%10)
                n = n // 10
            n = temp
            if(n in check):
                return False
            check[n] = 1
        return True
