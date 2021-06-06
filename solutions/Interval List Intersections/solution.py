class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i1 = 0
        i2 = 0
        ans = list()
        while(i1 < len(A) and i2<len(B)):
            x = A[i1]
            y = B[i2]
            
            if x[1] < y[0]:
                i1+=1
            elif y[1] < x[0]:
                i2+=1
            elif x[1] >= y[1]:
                ans.append([max(x[0],y[0]),y[1]])
                i2+=1
            elif y[1] > x[1]:
                ans.append([max(x[0],y[0]),x[1]])
                i1+=1
            # print(x,y,ans)
        return ans
