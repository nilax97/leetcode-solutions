class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        cow = 0
        values = dict()
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            elif secret[i] in values:
                values[secret[i]] += 1
            else:
                values[secret[i]] = 1
                
        for i in range(len(secret)):
            if secret[i] != guess[i]:
                if guess[i] in values:
                    if values[guess[i]] > 0:
                        cow +=1
                        values[guess[i]] -= 1
        return str(bull) + "A" + str(cow) + "B"
                        
