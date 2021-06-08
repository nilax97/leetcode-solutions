class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans = list()
        let = list()
        for x in s:
            ans.append(x)
            if x.isalpha():
                let.append(x)
        count = 0
        for i in range(len(ans)-1,-1,-1):
            if ans[i].isalpha():
                ans[i] = let[count]
                count += 1
        return "".join(ans)