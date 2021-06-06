class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        pos = dict()
        for i in range(len(S)):
            x = S[i]
            if x in pos:
                pos[x].append(i)
            else:
                pos[x] = [i]
        maxval = 0
        ans = list()
        previous = -1
        for i in range(len(S)):
            x = S[i]
            maxval = max(pos[x][-1],maxval)
            if maxval==i:
                ans.append(i-previous)
                previous = i
                maxval = i
        return ans
