class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = 0
        if(needle==""):
            return 0
        if(len(needle) > len(haystack)):
            return -1
        while index<(len(haystack) - len(needle) + 1):
            if haystack[index] == needle[0]:
                flag = 1
                for i in range(1,len(needle)):
                    if haystack[index+i] != needle[i]:
                        flag = 0
                        break
                if(flag==1):
                    return index
            index = index + 1
        return -1
