class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        sp = s.split()
        arr = []
        for  i in range(k) :
            arr.append(sp[i])
        return " ".join(arr)