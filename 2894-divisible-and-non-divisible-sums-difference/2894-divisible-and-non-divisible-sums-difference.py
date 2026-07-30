class Solution(object):
    def differenceOfSums(self, n, m):
        NewList = list(range(1,n+1))
        NewArr = list(filter(lambda arr : arr %m== 0 , NewList) ) 
        Sum_1= sum(NewArr)
        NewArr_1 = list(filter(lambda args: args  % m!= 0, NewList))
        Sum_2 = sum(NewArr_1)
        total = Sum_2 - Sum_1
        return total
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        