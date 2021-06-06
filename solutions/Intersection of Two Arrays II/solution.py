class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = dict()
        dict2 = dict()
        for x in nums1:
            if(x in dict1.keys()):
                dict1[x] += 1
            else:
                dict1[x] = 1
                
        for x in nums2:
            if(x in dict2.keys()):
                dict2[x] += 1
            else:
                dict2[x] = 1
                
        ans = list()
        for x in dict1.keys():
            if(x in dict2.keys()):
                times = min(dict1[x],dict2[x])
                for t in range(times):
                    ans.append(x)
        return ans
