class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts = sorted(horizontalCuts)
        verticalCuts = sorted(verticalCuts)
        max_w = max(horizontalCuts[0],h-horizontalCuts[-1])
        for i in range(len(horizontalCuts)):
                max_w = max(horizontalCuts[i] - horizontalCuts[i-1],max_w)
        max_h = 0
        max_h = max(verticalCuts[0],w-verticalCuts[-1])
        for i in range(len(verticalCuts)):
                max_h = max(verticalCuts[i] - verticalCuts[i-1],max_h)
        return (max_w * max_h) % ((10 ** 9) + 7)
        
