class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0 
        r = 0 
        subS = 0 
        mini = []
        while r < len(nums) :
            subS += nums[r] 

            while subS >= target :
                mini.append(r - l + 1)
                subS -= nums[l] 
                l += 1
            r += 1
            
        return 0 if len(mini) == 0 else min(mini)

        