class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        New_str = "".join(map(str , digits))
        Add = int(New_str ) + 1
        Empty_Arr = []
        for i  in str(Add):
            Empty_Arr.append(int(i))
        return Empty_Arr
        