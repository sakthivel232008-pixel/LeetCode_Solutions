class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        s = set()
        for  i in nums :
            if i in s :
                return True
                break
            s.add(i)
        return False


                
        