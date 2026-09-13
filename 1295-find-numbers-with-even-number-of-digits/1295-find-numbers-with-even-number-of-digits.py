class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        a = sum(1 for i in nums if len(str(i)) % 2 == 0)
        return a
        