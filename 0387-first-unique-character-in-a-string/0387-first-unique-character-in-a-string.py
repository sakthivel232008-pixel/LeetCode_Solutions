class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i , string  in enumerate(s) :
            if (s.count(string) < 2) :
                return i
                break
        else :
            return -1
                
        