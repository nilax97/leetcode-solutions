class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        s = A[0]
        i = 0
        for x in A:
            if x<s:
                if i==0:
                    i = -1
                elif i==1:
                    return False
            if x>s:
                if i==0:
                    i = 1
                elif i==-1:
                    return False
            s = x
        return True
