class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []
        for i  in nums1 :
            if ( i in nums2) :
                res.append(i)
                nums2.remove(i)

        return  res