class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        arr = []
        count = 0 
        for i in nums :
            count += i
            arr.append(count )
        return arr
        