class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        
        for i in range(min(len(v1),len(v2))):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
        for i in range(min(len(v1),len(v2)), max(len(v1),len(v2))):
            if i < len(v1):
                if v1[i]!= "0"*len(v1[i]):
                    return 1
            if i < len(v2):
                if v2[i] != "0"*len(v2[i]):
                    return -1
        return 0
