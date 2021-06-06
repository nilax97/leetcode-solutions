class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = list()
        val = path.split('/')
        for x in val:
            # print(x,ans)
            if x == '':
                continue
            if x == ".":
                continue
            if x == "..":
                if len(ans) != 0:
                    ans.pop(len(ans) - 1)
                continue
            ans.append(x)
        return '/' + '/'.join(ans)
