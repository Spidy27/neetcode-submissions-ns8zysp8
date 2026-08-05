class Solution:
    def countSubstrings(self, s: str) -> int:
        def is_palindrome(s):
            left = 0
            right = len(s)-1

            while left <= right:
                if s[left] != s[right]:
                    return False
        
                left += 1
                right -= 1
            return True    

        if len(s) == 0:
            return 0
    
        palindrome_count = 0
        count = 0
        left = 0
        right = len(s)-1

        for i in range(0, len(s)-1):
            if s[i] == s[i+1]:
                count += 1
                if i == len(s)-2:
                    break

        for char in s:
            count += 1

    
        while left < right:
            if s[left] == s[right]:
                palindrome_count += 1
            left += 1
            right -= 1    


        total_count = 0

        if is_palindrome(s):
            total_count = count + palindrome_count 
        else:
            total_count = count    

        return total_count

        