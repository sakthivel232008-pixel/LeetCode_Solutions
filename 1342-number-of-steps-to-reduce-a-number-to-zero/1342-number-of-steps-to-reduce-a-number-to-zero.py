class Solution:
    def numberOfSteps(self, num: int) -> int:
        count =  0
        curr = num 
        while curr != 0 :
            if(curr % 2  ==  0):
                curr //= 2 
                count += 1
            else :
                curr -= 1
                count += 1
        return count