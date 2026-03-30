class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i,j = 0,0
        dic = {}
        max_f = 0
        max_len = 0

        while j < len(s):
            dic[s[j]] = 1 + dic.get(s[j],0)
            max_f = max(max_f, dic[s[j]])
            length = j - i + 1
            changes = length - max_f
            if changes <= k:
                max_len = max(max_len, length)
            else:
                dic[s[i]] -= 1
                i += 1
            j += 1
        return max_len        

        