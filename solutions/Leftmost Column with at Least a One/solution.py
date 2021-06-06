# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        def col_search(binaryMatrix,i, m, n):
            left = 0
            right = n-1
            while(left<=right):
                mid = (left+right)//2
                # print(i, left,right,mid)
                if binaryMatrix.get(i,mid) == 0:
                    left = mid+1
                    continue
                else:
                    right = mid - 1
            if left == n:
                return n
            else:
                return (left+right)//2 + 1
        
        dims = binaryMatrix.dimensions()
        m = dims[0]
        n = dims[1]
        min_col = n
        for i in range(m):
            x = col_search(binaryMatrix,i, m, n)
            # print(i,x)
            if x < min_col:
                min_col = x
        if min_col == n:
            min_col = -1
        return min_col
