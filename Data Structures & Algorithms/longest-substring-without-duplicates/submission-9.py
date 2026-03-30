class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        left = 0
        max_count = 0

        for right, char in enumerate(s):
            if char in freq and freq[char] >= left:
                left = freq[char] + 1
            freq[char] = right
            max_count = max(max_count, right - left + 1)
        return max_count    
        