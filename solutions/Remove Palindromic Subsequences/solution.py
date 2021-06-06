class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0        #empty string 
        if s == s[::-1]:
            return 1 #palindrome
        return 2                  #general 
