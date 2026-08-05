class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memo = set()
        length = 0
        longest = 0
        for char in s:
            if char not in memo:
                length += 1
                memo.add(char)
                longest = max(longest, length)

            else:
                length = 0
                memo = set()    
        return longest