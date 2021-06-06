class Solution:
    def romanToInt(self, s: str) -> int:
        ans = list()
        conv = dict()
        conv['I'] = 1
        conv['V'] = 5
        conv['X'] = 10
        conv['L'] = 50
        conv['C'] = 100
        conv['D'] = 500
        conv['M'] = 1000
        for x in s:
            ans.append(conv[x])
        final = 0
        for i in range(len(ans)):
            if i == (len(ans) - 1):
                final += ans[i]
            elif ans[i] < ans[i+1]:
                final -= ans[i]
            else:
                final += ans[i]
        return final
        
