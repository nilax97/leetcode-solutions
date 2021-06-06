class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def checker(x):
            if x<10 and x>=0:
                return True
            return False
        def numcheck(n,k):
            if n==1:
                return ["0","1","2","3","4","5","6","7","8","9"]
            ans = list()
            val = numcheck(n-1,k)
            for x in val:
                a = int(x[0])+k
                b = int(x[0])-k
                if checker(a):
                    ans.append(str(a) + x)
                if checker(b):
                    ans.append(str(b) + x)
            return ans
        ans = numcheck(n,k)
        final_ans = list()
        for x in ans:
            if x[0] != '0':
                final_ans.append(x)
        return list(set(final_ans))
