class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        freq = {}
        count = 0
        max_count = 0

        for char in s:
            if char in freq:
                max_count = max(max_count, count)
                count = 0
            freq[char] = 1 + freq.get(char,0)
            count += 1

        return max_count       
        