class Solution:
    def isValid(self, s: str) -> bool:
        ans = list()
        for x in s:
            if x in ['(', '{', '[']:
                ans.append(x)
            elif x == ')':
                if len(ans) < 1:
                    return False
                if ans[-1] == '(':
                    ans.pop(-1)
                else:
                    return False
            elif x == ']':
                if len(ans) < 1:
                    return False
                if ans[-1] == '[':
                    ans.pop(-1)
                else:
                    return False
            elif x == '}':
                if len(ans) < 1:
                    return False
                if ans[-1] == '{':
                    ans.pop(-1)
                else:
                    return False
        if len(ans) > 0:
            return False
        return True
