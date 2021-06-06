class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        types = dict()
        ans = 0
        for x in candyType:
            if x not in types:
                types[x] = 1
                ans += 1
        return min(len(candyType)//2,ans)
