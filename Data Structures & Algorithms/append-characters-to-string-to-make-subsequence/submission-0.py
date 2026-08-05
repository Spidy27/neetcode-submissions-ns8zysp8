class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if len(s) == len(t):
            return 0

        x = y = 0
        count = 0

        while y < len(t) and x < len(s):
            if s[x] == t[y]:
                count += 1
            x += 1
            y += 1
        return len(t[count:])            
        