class Solution:
    def isNumber(self, s: str) -> bool:
        if "inf" in s.lower():
            return False
        try: float(s)
        except ValueError: return False
        else: return True
