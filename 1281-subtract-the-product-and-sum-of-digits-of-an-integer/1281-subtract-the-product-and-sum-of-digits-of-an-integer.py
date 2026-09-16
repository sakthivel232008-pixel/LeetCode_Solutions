class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        res = 0 
        sum1 =  0
        product = 1
        for  i in str(n):
            sum1 += int(i)
            product *= int(i)
        res = product - sum1
        return res  


        