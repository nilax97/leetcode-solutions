from functools import cmp_to_key

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def comparator(x,y):
            for i in range(len(mat[x])):
                if mat[x][i] > mat[y][i]:
                    return 1
                elif mat[x][i] < mat[y][i]:
                    return -1
            if x > y:
                return 1
            else:
                return -1
        ans = [0] * len(mat)
        for i in range(len(mat)):
            ans[i] = i
        ans = sorted(ans, key=cmp_to_key(comparator))
        return ans[:k]
