class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        val = dict()
        for b in B:
            val2 = dict()
            for x in b:
                if x in val2:
                    val2[x] += 1
                else:
                    val2[x] = 1
            for x in val2.keys():
                if x in val:
                    val[x] = max(val[x],val2[x])
                else:
                    val[x] = val2[x]
        ans = list()
        for a in A:
            val2 = dict()
            for x in a:
                if x in val2:
                    val2[x] += 1
                else:
                    val2[x] = 1
            flag = 0
            for x in val.keys():
                if x not in val2:
                    flag = 1
                    break
                if val2[x] < val[x]:
                    flag = 1
                    break
            if flag == 0:
                ans.append(a)
        return ans
                
