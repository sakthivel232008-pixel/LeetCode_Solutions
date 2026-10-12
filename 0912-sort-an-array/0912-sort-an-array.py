import random
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def QuickSort(arr) :
            if len(arr) <= 1 :
                return arr
            l = []            
            r = []            
            m = []            

            pivot =  random.choice(arr)

            for  i in arr :
                if i == pivot :
                    m.append(i)
                elif i < pivot :
                    l.append(i)
                else :
                    r.append(i)
            return QuickSort(l) + m + QuickSort(r)

       
        return  QuickSort(nums)
                    