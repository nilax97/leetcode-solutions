class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n>12 or n<4:
            return []
        def check(s):
            if int(s[0])==0 and int(s)!=0:
                return False
            if int(s)==0 and len(s)!=1:
                return False
            if int(s)<256:
                return True
            else:
                return False
        ans = list()
        for i in range(1,n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    one = s[:i]
                    two = s[i:j]
                    three = s[j:k]
                    four = s[k:]
                    print(one,two,three,four,check(one) and check(two) and check(three) and check(four))
                    if check(one) and check(two) and check(three) and check(four):
                        ans.append(one + "." + two + "." + three + "." + four)
        return ans
                    
                
