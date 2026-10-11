class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        str1 = ""
        str2 = ""
        for  i in word1 :
            str1 += i
        
        for j in word2 :
            str2 += j

        if (str1 == str2) :
            return True

        else :
            return False