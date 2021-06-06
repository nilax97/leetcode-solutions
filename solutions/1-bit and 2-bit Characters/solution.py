class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) == 0:
            return False
        if len(bits) == 1:
            if bits[0] == 1:
                return False
            return True
        if len(bits) == 2:
            if bits[0] == 1:
                return False
            if bits[1] == 1:
                return False
            return True
        
        if bits[0] == 1:
            return self.isOneBitCharacter(bits[2:])
        else:
            return self.isOneBitCharacter(bits[1:])
