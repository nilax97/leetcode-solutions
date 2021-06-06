class Solution:
    def isUgly(self, num: int) -> bool:
        def ugly(num):
            if num <=0:
                return False
            if abs(num)<2:
                return True
            if num == 2 or num == 3 or num == 5:
                return True
            if num % 2 == 0:
                return ugly(num // 2)
            if num % 3 == 0:
                return ugly(num // 3)
            if num % 5 == 0:
                return ugly(num // 5)
            return False
        return ugly(num)
