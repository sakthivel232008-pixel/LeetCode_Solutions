class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        arr = []
        for i in nums :
            if(nums.count(i) > 1 ) :
                arr.append(i)
        return list(set(arr))
        
        