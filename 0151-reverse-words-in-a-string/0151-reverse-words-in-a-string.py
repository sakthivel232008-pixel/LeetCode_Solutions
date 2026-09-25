class Solution:
    def reverseWords(self, s: str) -> str:
        s1 = s.split()
        res = " ".join(s1[::-1])
        return res