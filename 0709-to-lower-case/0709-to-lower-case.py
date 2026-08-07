class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = []
        for i in s:
            arr.append(i.lower())

        New_arr = "".join(arr)
        return New_arr
        