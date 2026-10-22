class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        arr = []
        for  i in range (left  , right + 1 ) :
            temp = i
            v = True 
            while temp > 0 :
                digit = temp % 10

                if digit == 0 or i % digit != 0 :
                    v = False
                    break
                temp //= 10
            if v :
                arr.append(i)        
        return arr