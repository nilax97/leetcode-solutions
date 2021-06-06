class Solution:
    def myAtoi(self, str: str) -> int:
        def isnum(x):
            if(ord('0') <= ord(x) and ord('9')>=ord(x)):
                return True
            return False
        
        str = str.strip()
        neg = 1
        flag = 1
        num = 0
        for x in str:
            if(x == '-' and flag==1):
                neg = -1
                flag = 0
                continue
            if(x == '+' and flag==1):
                neg = 1
                flag = 0
                continue
            flag = 0
            if not isnum(x):
                break
            num += ord(x) - ord('0')
            num = num*10
        
        num = num//10 * neg
        if(num < -(2**31)):
            num = -2**31
        if(num > (2**31 -1)):
            num = 2**31 - 1
        return num
        
