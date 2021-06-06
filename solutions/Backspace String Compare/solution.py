class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        l1 = len(S)
        l2 = len(T)
        i = 0
        while(i<l1):
            print(S,S[i])
            if S[i] == '#':
                if(i==0):
                    S = S[i+1:]
                    l1 = l1 - 1
                    i = i - 1
                else:
                    S = S[:i-1] + S[i+1:]
                    i = i-2
                    l1 = l1 -2
            i = i+1
            if(i<0):
                i==0
        i = 0
        print(" _____ ")
        while(i<l2):
            print(T,T[i])
            if T[i] == '#':
                if(i==0):
                    T = T[i+1:]
                    l2 = l2 - 1
                    i = i - 1
                else:
                    T = T[:i-1] + T[i+1:]
                    i = i-2
                    l2 = l2 -2
            i = i+1
            if(i<0):
                i==0
        print(S,T)
        if(S==T):
            return True
        return False
