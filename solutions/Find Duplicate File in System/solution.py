class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        val = []
        for temp in paths:
            name = temp.split(" ")
            x = name[0]
            for i in range(1,len(name)):
                val.append(x + "/" + name[i])
        ans = dict()
        for a in val:
            x = a.split("(")
            x1 = x[0]
            x2 = x[1][:-1]
            if x2 in ans:
                ans[x2].append(x1)
            else:
                ans[x2] = [x1]
        ret = []
        for x in list(ans.keys()):
            if len(ans[x]) > 1:
                ret.append(ans[x])
        return ret
                
            
