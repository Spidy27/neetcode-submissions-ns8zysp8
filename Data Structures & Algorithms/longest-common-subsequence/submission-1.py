class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        i = 0
        j = 0
        char_count = 0
        while i < len(text1) and j < len(text2):
            if text2[j] != text1[i]:
                i += 1
            else:
                char_count += 1
                j += 1

        return char_count
                    