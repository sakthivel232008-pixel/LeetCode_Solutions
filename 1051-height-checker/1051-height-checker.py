class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        s = sorted(heights) 
        count = 0
        for  i in range(len(s)) :
            if s[i] != heights[i] :
                count += 1
        return count 





