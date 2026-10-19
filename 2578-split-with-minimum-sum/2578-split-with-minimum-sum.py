class Solution:
    def splitNum(self, num: int) -> int:
        odd = ""
        even = "" 
        for  index  , i  in enumerate (sorted(str(num))) :
            if index % 2 == 0 :
                even +=  (i)
            else :
                 odd +=  (i)

        return  int(odd) + int (even)
        

        