class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def happy(n):
            if n==1:
                return ["a","b","c"]
            val = happy(n-1)
            ans = list()
            for x in val:
                if x[-1] == "a":
                    ans.append(x + "b")
                    ans.append(x + "c")
                if x[-1] == "b":
                    ans.append(x + "a")
                    ans.append(x + "c")
                if x[-1] == "c":
                    ans.append(x + "a")
                    ans.append(x + "b")
            return ans
        ans = happy(n)
        if len(ans) < k:
            return ""
        else:
            return ans[k-1]
