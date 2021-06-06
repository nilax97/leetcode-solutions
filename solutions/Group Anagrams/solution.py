class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = dict()
        for x in strs:
            temp = "".join(sorted([char for char in x]))
            if(temp in ans.keys()):
                ans[temp].append(x)
            else:
                ans[temp] = [x]
        sol = list()
        for x in ans.keys():
            sol.append(ans[x])
        return sol
