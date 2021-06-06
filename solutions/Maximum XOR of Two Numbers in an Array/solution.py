class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        trie = {}
        for x in nums: 
            s = bin(x)[2:].zfill(32)
            node = oppo = trie 
            for c in map(int, s): 
                node = node.setdefault(c, {}) # add to trie
                oppo = oppo.get(1-c) or oppo.get(c) # as "opposite" as possible
            node["#"] = x
            ans = max(ans, x^oppo["#"])
        return ans
