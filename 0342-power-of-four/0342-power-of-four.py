class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1 :
            return True
        
        elif n % 4 != 0 :
            return False

        else :
            p  = 1
            while p <= n :
                if p == n :
                    return True
                    break
                p *= 4
            else :
                return False
            
        