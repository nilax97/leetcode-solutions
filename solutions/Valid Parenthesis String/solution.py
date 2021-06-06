class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin = 0
        cmax = 0
        for x in s:
            if x == '(':
                cmin += 1
                cmax += 1
                continue
            if x == ')':
                cmin = max(cmin-1,0)
                cmax -= 1
            if x == '*':
                cmax += 1
                cmin = max(cmin-1,0)
            if cmax < 0:
                return False
        return cmin == 0
                
