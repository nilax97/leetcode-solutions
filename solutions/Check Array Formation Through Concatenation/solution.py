class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        val = dict()
        for x in pieces:
            val[x[0]] = x
        
        while len(arr) > 0:
            if arr[0] in val:
                temp = arr[0]
                for x in val[temp]:
                    if len(arr) == 0:
                        return False
                    if x == arr[0]:
                        arr.pop(0)
                    else:
                        return False
            else:
                return False
        return True
            
