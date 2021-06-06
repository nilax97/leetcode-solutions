class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        ans = set()
        for i in range(bound):
            if pow(x,i) > bound or (x==1 and i>0):
                break
            for j in range(bound):
                if pow(y,j) > bound or (y==1 and j>0):
                    break
                temp = pow(x,i) + pow(y,j)
                # print(temp)
                if temp <= bound:
                    ans.add(temp)
        return list(ans)
