class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        a_sum = 0 
        b_sum = 0 
        for  i in nums :
            if i > 9:
                a_sum += i
            if i < 10 :
                b_sum += i

        if a_sum == b_sum :
            return False
        if a_sum > b_sum :
            return True
        elif b_sum > a_sum :
            return True

