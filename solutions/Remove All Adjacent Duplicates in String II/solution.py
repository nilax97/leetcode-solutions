class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        distinct = set(s)
        toRemove = list()
        for char in distinct:
            toRemove.append(char*k)
        
        while True:
            start = s
            for dup in toRemove:
                if dup in s:
                    s = s.replace(dup, "")
            if start == s:
                return s
