class OneBit:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if len(bits) == 1: 
            return True 
        
        s = 0
        i = len(bits) - 2
        
        while bits[i] == 1 and i >= 0:
            s += 1
            i -= 1
        return s%2 == 0
