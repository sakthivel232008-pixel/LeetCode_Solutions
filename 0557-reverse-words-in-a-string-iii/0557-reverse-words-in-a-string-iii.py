class Solution:
    def reverseWords(self, s: str) -> str:
        n_split = s.split()
        str1  = ""
        for  i in n_split:
            s1 = "".join(i)
            str1 += s1[::-1] + " "
        
        return  str1.strip()
  
        
        