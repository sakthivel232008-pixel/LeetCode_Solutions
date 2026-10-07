class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        arr = []
        for  ind , i in  enumerate(words) :
            for j  in i :
                if (j == x) :
                    arr.append(ind)
                
        return list(set(arr))