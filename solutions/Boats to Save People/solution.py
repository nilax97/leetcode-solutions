class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        weight = dict()
        for x in people:
            if x in weight:
                weight[x] += 1
            else:
                weight[x] = 1
        ans = 0
        for x in people:
            if weight[x] > 0:
                weight[x]-= 1
                upper = limit - x
                for i in range(upper,0,-1):
                    if i in weight:
                        if weight[i] > 0:
                            weight[i] -= 1
                            break
                ans += 1
            else:
                continue
        return ans
