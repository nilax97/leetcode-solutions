class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        def prime_check(x):
            for i in range(2,int(sqrt(x)+1)):
                if x%i==0:
                    return False
            return True
           
        for i in range(2,n+1):
            if prime_check(i)==False:
                continue
            l = s[0:int(n/i)]
            # print(i,l)
            if l*i == s:
                return True
        return False
