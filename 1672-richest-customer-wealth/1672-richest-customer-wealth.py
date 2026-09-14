class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        high = 0
        for i in accounts:
            tot = sum(i)
            if(tot > high ):
                high = tot

        return high
        