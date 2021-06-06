class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def make_seq(s,l,h,ans):
            if (int(s[0]) + len(s))>10:
                return ans
            x = s[0]
            for i in range(1,len(s)):
                x = x + str(int(x[-1]) + 1)
            # print(x,s,l,h,ans)
            if l<= int(x) and h>= int(x): 
                ans.append(int(x))
            return ans
        l = len(str(low))
        h = len(str(high))
        ans = list()
        for i in range(l,h+1):
            s = "0" * (i-1)
            for i in range(1,10):
                ans = make_seq(str(i) + s,low,high,ans)
        return ans
