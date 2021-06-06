class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        nums, lis = [j for _, j in envelopes], []
        for current in nums:
            idx = bisect.bisect_left(lis, current)
            lis[idx:idx+1] = [current]
        return len(lis)
