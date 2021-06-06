class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        start = 1
        for x in arr:
            while start < x:
                if k == 1:
                    return start
                k -= 1
                start += 1
            start+= 1
        return arr[-1] + k
            
