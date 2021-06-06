class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = s.split(" ")
        words2 = list()
        for i in range(len(words)):
            words2.append(words[i].strip())
            if len(words2[-1]) == 0:
                words2.pop(-1)
        print(words2)
        return " ".join(reversed(words2))
