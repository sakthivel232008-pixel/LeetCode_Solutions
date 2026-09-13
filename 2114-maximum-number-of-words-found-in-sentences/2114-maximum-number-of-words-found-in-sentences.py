class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_count = 0
        for i in sentences:
            new_count = i.count(" ")
            if(new_count > max_count):
                max_count = new_count 
        return(max_count +1)
        