# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        current = head
        a = []
        while current != None:
            a.append(str(current.val))
            current = current.next
        new_join = "".join(a)
        res = 0 
        expo = len(new_join) - 1
        for i  in new_join:
            res =  res + int(i)  * 2 **expo
            expo -= 1
        return res

        