class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        count1 = {}
        count2 = {}
        for char in text1:
            count1[char] = 1 + count1.get(char,0)

        for char in text2:
            count2[char] = 1 + count2.get(char,0)

        common = set(count1.keys()) & set(count2.keys())
        return len(common)        
        