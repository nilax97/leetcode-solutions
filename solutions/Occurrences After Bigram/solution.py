class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        val = text.split(" ")
        ans = []
        for i in range(len(val) - 2):
            if val[i] == first and val[i+1] == second:
                ans.append(val[i+2])
        return ans
            
