class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = list()
        flag = 0
        for x in intervals:
            if x[1] < newInterval[0]:
                ans.append(x)
            elif x[0] > newInterval[1]:
                if flag==0:
                    ans.append(newInterval)
                    flag = 1
                ans.append(x)
            elif flag==0:
                x[0] = min(x[0], newInterval[0])
                x[1] = max(x[1],newInterval[1])
                ans.append(x)
                flag = 1
            if flag==1 and x[0] <= ans[-1][1]:
                # print("Inserting", ans[-1][1],x[1])
                ans[-1][1] = max(ans[-1][1], x[1])
            # print(ans,flag,x)
        if flag==0:
            ans.append(newInterval)
        return ans
