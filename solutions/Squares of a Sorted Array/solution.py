class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        neg = []
        pos = []
        ans = []
        for x in nums:
            if x < 0:
                neg.append(x*x)
            else:
                pos.append(x*x)
        neg = neg[::-1]
        i = 0
        j = 0
        n = len(neg)
        m = len(pos)
        while(True):
            if i==n and j==m:
                break
            if i==n and j<m:
                ans.append(pos[j])
                j += 1
                continue
            if j==m and i<n:
                ans.append(neg[i])
                i += 1
                continue
            if neg[i] < pos[j]:
                ans.append(neg[i])
                i += 1
                continue
            ans.append(pos[j])
            j += 1
            continue
        return ans
            
                
