class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = [char.lower() for char in s if char.isalnum()]
        if new_s == new_s[::-1]:
            return True 
        else:
            return False
        