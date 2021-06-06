class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def permute(x,ans):
            if x.isalpha():
                val = [x.lower(),x.upper()]
            else:
                val = [x]
            final_ans = list()
            if len(ans) == 0:
                return val
            for a in ans:
                for b in val:
                    final_ans.append(a+b)
            return final_ans
        ans = []
        for x in S:
            ans = permute(x,ans)
        return ans
