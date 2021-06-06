class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def div_check(x):
            y = x
            while(y>0):
                a = y%10
                if a==0:
                    return False
                if x % a != 0:
                    return False
                y = y//10
            return True
        ans = list()
        for i in range(left,right+1):
            if div_check(i):
                ans.append(i)
                
        return ans
