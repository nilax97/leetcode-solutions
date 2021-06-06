class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        ans = [""] * len(S)
        for i in range(len(S)):
            ans[i] = S[i]
        for i in range(len(indexes)):
            start = indexes[i]
            src = sources[i]
            change = 1
            for j in range(len(src)):
                if S[start + j] != src[j]:
                    change = 0
                    break
            if change == 0:
                continue
            ans[start] = targets[i]
            for j in range(1,len(src)):
                ans[start + j] = ""
        return "".join(ans)
