def cns(n):
    if(n==1):
        return "1"
    s = cns(n-1)
    curr = s[0]
    count = 0
    ans = ""
    for x in s:
        if(x==curr):
            count +=1
        else:
            ans = ans + str(count) + curr
            count = 1
            curr = x
    ans = ans + str(count) + curr
    return ans

class Solution:
    def countAndSay(self, n: int) -> str:
        return cns(n)
