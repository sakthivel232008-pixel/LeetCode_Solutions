class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if (n == 1):
            return True
        elif n % 3 != 0 :
            return False
        else : 
            power = 1
            while power <= n :
                if power == n :
                    return True
                    break
                power *= 3 
            else :
                return False
        