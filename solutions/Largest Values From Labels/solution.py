class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        lab = dict()
        n = len(values)
        vals = [0] * n
        for i in range(n):
            vals[i] = i
        vals = sorted(vals, key=lambda x:values[x], reverse=True)
        ans = 0
        for x in range(n):
            if num_wanted == 0:
                break
            i = vals[x]
            l = labels[i]
            v = values[i]
            if l not in lab:
                lab[l] = 1
                ans += v
                num_wanted -= 1
            elif lab[l] < use_limit:
                lab[l] += 1
                ans += v
                num_wanted -= 1
        return ans
