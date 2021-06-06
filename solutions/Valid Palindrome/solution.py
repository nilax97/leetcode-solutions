class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def isalnum(x):
            if(ord('a') <= ord(x) and ord('z')>=ord(x)):
                return True
            if(ord('0') <= ord(x) and ord('9')>=ord(x)):
                return True
            return False
        
        start = 0
        end = len(s)-1
        s = s.lower()
        while(start<end):
            print(s[start],s[end])
            if not isalnum(s[start]):
                start +=1
                continue
            if not isalnum(s[end]):
                end -=1
                continue
            if s[start]==s[end]:
                start +=1
                end -=1
                continue
            return False
        return True
        
