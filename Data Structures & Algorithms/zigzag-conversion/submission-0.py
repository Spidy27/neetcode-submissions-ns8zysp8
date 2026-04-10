class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        res = ["" for _ in range(numRows)]
        curIdx = 0
        direction = 1
        j = 0

        while j < len(s):
            res[curIdx] += s[j]
            if curIdx == 0:
                direction = 1
            elif curIdx == numRows - 1:
                direction = -1

            curIdx += direction
            j += 1

        ans = ""
        for string in res:
            ans += string

        return ans                    

        