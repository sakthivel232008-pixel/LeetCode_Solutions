class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        d =  {}
        for  i in nums :
            if i in d :
                d[i] += 1

            else :
                d[i] = 1
        tot = 0
        for  i , j in  d.items() :
            if j < 2 :
                tot += i

        return tot

        