class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","
            ...","-","..-","...-",".--","-..-","-.--","--.."];
        types = set();
        for word in words:
            trans = "";
            for w in word:
                value = ord(w) - ord('a')
                trans = trans + morse[value];
            types.add(trans)
        return len(types);
        
