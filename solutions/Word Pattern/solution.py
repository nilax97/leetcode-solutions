class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split(" ")
        if len(pattern) != len(words):
            return False
        check1 = dict()
        check2 = dict()
        for i in range(len(pattern)):
            key = pattern[i]
            value = words[i]
            if key in check1:
                if check1[key] != value:
                    return False
            else:
                check1[key] = value
            if value in check2:
                if check2[value] != key:
                    return False
            else:
                check2[value] = key
        return True
