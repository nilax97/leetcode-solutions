class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        ans = list()
        for i in range(len(words)):
            check = 1
            x = words[i]
            for j in range(len(ans)):
                y = ans[j]
                if x.endswith(y):
                    ans[j] = x
                    check = 0
                    break
                elif y.endswith(x):
                    check = 0
                    break         
            if check == 1:
                ans.append(x)
        print(ans)
        return len("#".join(ans) + "#")
                
