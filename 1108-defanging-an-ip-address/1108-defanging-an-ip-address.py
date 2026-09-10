class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_re = address.replace("." , "[.]")
        return new_re
        