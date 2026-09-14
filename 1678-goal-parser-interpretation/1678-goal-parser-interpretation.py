class Solution:
    def interpret(self, command: str) -> str:
        arr = []
        new_append = arr.append(command.replace("()" , "o").replace("(al)" , "al"))
        new_join = "".join(arr)
        return new_join
        