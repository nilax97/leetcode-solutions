class Solution:
    def reverseVowels(self, s: str) -> str:
        ans = list()
        vow = list()
        for x in s:
            ans.append(x)
            if x in ['a','e','i','o','u','A','E','I','O','U']:
                vow.append(x)
        for i in range(len(ans)):
            if ans[i] in ['a','e','i','o','u','A','E','I','O','U']:
                ans[i] = vow.pop(-1)
        return "".join(ans)
