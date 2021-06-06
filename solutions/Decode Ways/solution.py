class Solution:
    def numDecodings(self, s: str) -> int:
        values = dict()
        def decode(s,values):
            if s in values:
                return values[s]
            n = len(s)
            if n==0:
                ans = 1
                values[s] = ans
                return ans
            x = int(s[0])
            if n==1:
                if x > 0:
                    ans = 1
                else:
                    ans = 0
                values[s] = ans
                return ans
            y = int(s[1])
            if x == 1:
                if y > 0:
                    ans = decode(s[1:],values) + decode(s[2:],values)
                else:
                    ans = decode(s[2:],values)
            elif x == 2:
                if y==0:
                    ans = decode(s[2:],values)
                if y<7:
                    ans = decode(s[1:],values) + decode(s[2:],values)
                else:
                    ans = decode(s[1:],values)
            elif x == 0:
                ans = 0
            else:
                ans = decode(s[1:],values)
            values[s] = ans
            return ans
        return decode(s,values)
