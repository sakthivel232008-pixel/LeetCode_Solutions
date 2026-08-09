class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        Fill = list(filter (lambda args : args.isalnum() , s))
        str_1 = "".join(Fill).lower()
        str_2 = str_1[::-1]
        if(str_1 == str_2):
            return True
        else:
            return False
        