class Solution:
    def customSortString(self, S: str, T: str) -> str:
        val = dict()
        ans = []
        for x in T:
            if x not in S:
                ans.append(x)
                continue
            if x in val:
                val[x] += 1
            else:
                val[x] = 1
        for x in S:
            if x not in val:
                continue
            ans = ans + [x] * val[x]
        print(ans)
        return "".join(ans)
        
