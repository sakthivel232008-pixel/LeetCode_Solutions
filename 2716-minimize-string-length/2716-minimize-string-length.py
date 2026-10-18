class Solution:
    def minimizedStringLength(self, s: str) -> int:
        s1 = []
        for  i in s :
            s1.append(i)

        return len(set(s1))

        