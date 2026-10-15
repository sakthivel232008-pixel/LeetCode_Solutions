class Solution:
    def numberOfMatches(self, n: int) -> int:
        t = 0
        while n > 1 :
            m = n // 2
            t += m
            n = n - m
        return t