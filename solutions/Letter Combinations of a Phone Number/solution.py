class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = dict()
        map["2"] = ["a","b","c"]
        map["3"] = ["d","e","f"]
        map["4"] = ["g","h","i"]
        map["5"] = ["j","k","l"]
        map["6"] = ["m","n","o"]
        map["7"] = ["p","q","r","s"]
        map["8"] = ["t","u","v"]
        map["9"] = ["w","x","y","z"]
        
        ans = [""]
        for d in digits:
            temp = list()
            cur = map[d]
            for x in ans:
                for c in cur:
                    temp.append(x+c)
            ans = temp
        if(ans[0]==""):
            return []
        return ans
