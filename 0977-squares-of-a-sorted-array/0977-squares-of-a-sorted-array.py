class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        Filter = list(map(lambda args : args **2 , nums))
        return sorted(Filter)
        