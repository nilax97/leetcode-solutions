class Solution:
    def reverse(self, x: int) -> int:
        neg = 1
        if(x<0):
            neg = -1
            x = abs(x)
        if(x> (2**31 -1)):
            return 0
        s = list()
        while(x>0):
            s.append(x%10)
            x = x//10
        ans = 0
        print(s)
        for x in s:
            ans += x
            ans *= 10
        ans = ans//10
        if(ans > (2**31 -1)):
            return 0
        return neg * ans
