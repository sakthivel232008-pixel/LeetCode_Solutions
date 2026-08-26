class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_1 = s.split()
        last = list_1.pop(-1)
        return len(last)
        