class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = {""}
        for c in tiles:
            res |= {d[:i] + c + d[i:] for d in res for i in range(len(d)+1)}
        print(res)
        return len(res) - 1
