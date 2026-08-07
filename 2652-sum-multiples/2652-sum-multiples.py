class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        List_1 = list(range(1,n+1))
        Empty_List  = []
        Filter = list(filter(lambda args: (args % 3 == 0 ) ,List_1))
        Filter_1 = list(filter(lambda args: (args % 5 == 0 ) ,List_1))
        Filter_2 = list(filter(lambda args: (args % 7 == 0 ) ,List_1))
        Empty_List.extend(Filter)
        Empty_List.extend(Filter_1)
        Empty_List.extend(Filter_2)
        List_to_Set = set(Empty_List)
        return sum(List_to_Set)
        