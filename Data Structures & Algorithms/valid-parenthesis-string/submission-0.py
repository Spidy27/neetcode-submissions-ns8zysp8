class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        open_count = 0
        available = s.count("*")

        for char in s:
            if char == "(":
                open_count += 1

            if char == ")":
                open_count -= 1 

        if open_count == 0:
            return True

        for i in range(available):
            if open_count < 0 and available != 0:
                open_count += 1
                available -= 1

            if open_count > 0 and available != 0:
                open_count -= 1
                available -= 1

            if open_count == 0:
                return True

        return False                

        