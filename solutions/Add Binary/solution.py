class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n1 = len(a)
        n2 = len(b)
        n = max(n1,n2) + 1
        ans = [0] * n
        x = 0
        for i in range(n):
            i1 = n1 - i - 1
            i2 = n2 - i - 1
            if  i1 >= 0 and a[i1] == '1':
                x += 1
            if i2 >= 0 and b[i2] == '1':
                x += 1
            ans[n - i - 1] = str(x % 2)
            x = x // 2
        if ans[0] == '0':
            ans.pop(0)
        return "".join(ans)
