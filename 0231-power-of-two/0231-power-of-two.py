class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if(n == 1 ):
            return True
        
        elif (n % 2 != 0):
            return False
    
        else:
            power = 1 
            while power <= n :
                if(power == n):
                    return True
                    
                power *= 2
            else:
                return False
        