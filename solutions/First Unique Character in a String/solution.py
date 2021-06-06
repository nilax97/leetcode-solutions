class Solution:
    def firstUniqChar(self, s: str) -> int:
        check = dict()
        for i in range(len(s)):
            if s[i] not in check.keys():
                check[s[i]] = [i]
            else:
                check[s[i]].append(i)
        for x in check.keys():
            if len(check[x])==1:
                return check[x][0]
        return -1
