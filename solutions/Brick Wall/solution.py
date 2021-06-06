class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        d = collections.defaultdict(int)
        for line in wall:
            i = 0
            for brick in line[:-1]:
                i += brick
                d[i] += 1
        # print len(wall), d
        return len(wall)-max(list(d.values())+[0])
