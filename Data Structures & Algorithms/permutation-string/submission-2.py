class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = 0
        maxCount = 0
        for char in s2:
            if char in s1:
                count += 1
                maxCount = max(maxCount, count)
            else:
                count = 0    
        
        if maxCount == len(s1):
            return True

        return False    