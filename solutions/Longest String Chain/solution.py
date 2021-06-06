class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        if len(words) < 2:
            return len(words)
        words = sorted(words, key=lambda w: len(w),reverse=True)
        val = dict()
        for w in words:
            val[w] = 1
        ans = 1
        for w in words:
            for i in range(len(w)):
                key = w[:i] + w[i+1:]
                if key in val:
                    val[key] = max(val[w] +1, val[key])
                    ans = max(ans,val[key])
        return ans
                
        
