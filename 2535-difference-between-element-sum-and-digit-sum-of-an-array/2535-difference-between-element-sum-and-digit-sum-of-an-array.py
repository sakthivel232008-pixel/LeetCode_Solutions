class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]   
        :rtype: int
        """
        Empty_num = 0
        total = 0
        for i in nums:
            while i > 0:
                digit  = i % 10
                Empty_num+= digit
                i = i //10
        for i in nums:
            total += i
        Final = total - Empty_num
        return Final