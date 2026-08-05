class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) == 1 and nums[0] == 1:
            return 1
        left = count = max_count = 0
        while left < len(nums):
            if nums[left] != 1:
                count = 0
            count += 1
            max_count = max(max_count, count)
            left += 1
        return max_count - 1       
        