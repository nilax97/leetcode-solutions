class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        index = 0
        if(len(strs)==0):
            return ""
        while(True):
            flag = 1
            if(index>=len(strs[0])):
                break
            for i in range(1,len(strs)):
                if(index>=len(strs[i])):
                    flag = 0
                    break
                if strs[i-1][index] != strs[i][index]:
                    flag = 0
                    break
            if(flag==0):
                break
            index +=1
        return strs[0][0:index]
