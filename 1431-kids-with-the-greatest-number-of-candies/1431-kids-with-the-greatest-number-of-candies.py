class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        arr  = []
        b = []
        for  i in candies :
            i += extraCandies
            arr.append(i)
        for i in arr :
            if ( i >= max(candies)) :
                b.append(True)
            else :
                b.append(False)
        return b
             