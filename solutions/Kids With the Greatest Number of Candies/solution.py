class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        goal = -1
        for x in candies:
            goal = max(goal,x)
        ans = list()
        for x in candies:
            if (x+extraCandies) >= goal:
                ans.append(True)
            else:
                ans.append(False)
        return ans
