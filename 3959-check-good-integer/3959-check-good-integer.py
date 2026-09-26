class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        tot = 0
        sq = 0 
        for i in str(n) :
            tot += int(i)
            s = int(i) ** 2 
            sq += s
        res = sq - tot 
        if(res >= 50) :
            return True
        else :
            return  False