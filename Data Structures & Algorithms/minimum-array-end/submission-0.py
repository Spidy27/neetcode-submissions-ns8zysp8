class Solution:
    def minEnd(self, num: int, x: int) -> int:
        temp = x
        res = []
        res.append(temp)

        for i in range(num-1):
            temp = (temp + 1) | x
            res.append(temp)
        return temp    
        