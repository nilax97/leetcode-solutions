class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        ele = dict()
        for x in arr:
            if x in ele:
                ele[x] += 1
            else:
                ele[x] = 1
        for x in ele.keys():
            if x+1 in ele:
                count += ele[x]
        return count
                
