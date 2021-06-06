class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
                
        def msbPos(n):  
          
            msb_p = -1
            while (n > 0):  
              
                n = n >> 1
                msb_p += 1
              
            return msb_p  
          
        # Function to find Bit-wise & of  
        # all numbers from x to y.  
        def andOperator(x, y):  
          
            res = 0 # Initialize result  
          
            while (x > 0 and y > 0):  
              
                # Find positions of MSB in x and y  
                msb_p1 = msbPos(x)  
                msb_p2 = msbPos(y)  
          
                # If positions are not same, return  
                if (msb_p1 != msb_p2):  
                    break
          
                # Add 2^msb_p1 to result  
                msb_val = (1 << msb_p1)  
                res = res + msb_val  
          
                # subtract 2^msb_p1 from x and y.  
                x = x - msb_val  
                y = y - msb_val  
          
            return res
        return andOperator(m,n)
            
