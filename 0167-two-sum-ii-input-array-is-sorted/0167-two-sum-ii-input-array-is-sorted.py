class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l = 0 
        r = len(numbers) - 1
        s = 0
        while r < len(numbers) :
            s = numbers[l] + numbers[r] 
            if s == target :
                return [l+1 , r + 1]

            elif s > target  :
                r -= 1
            
            else :
                l += 1


        