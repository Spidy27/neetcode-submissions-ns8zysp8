class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 1
        minSize = float('inf')

        while right <= len(nums):
            if sum(nums[left:right]) >= target:
                size = right - left
                minSize = min(minSize, size)
                left += 1
            else:
                right += 1

        if minSize != float('inf'):
            return minSize

        return 0                
        