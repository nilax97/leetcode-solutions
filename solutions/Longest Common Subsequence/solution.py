class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        answers = dict()
        def longseq(text1, text2):
            if (text1,text2) in answers:
                return answers[text1,text2]
            # print(text1,",",text2)
            if len(text1) == 0 or len(text2) == 0:
                return 0
            if text1[-1] == text2[-1]:
                x = longseq(text1[:-1],text2[:-1])
                answers[(text1,text2)] = 1+x
                return 1 + x
            else:
                a = longseq(text1[:-1],text2)
                b = longseq(text1,text2[:-1])
                answers[(text1,text2)] = max(a,b)
                return max(a,b)
        
        return longseq(text1,text2)
