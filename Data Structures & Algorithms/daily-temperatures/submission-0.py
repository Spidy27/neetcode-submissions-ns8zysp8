class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        dp = [0] * len(temperatures)

        left = 0
        right = 0
        count = 0
        while right < len(temperatures):
            if temperatures[right] > temperatures[left]:
                dp[left] = count
                count = 0
                left += 1
                right = left

            count += 1
            right += 1

        return dp        
        