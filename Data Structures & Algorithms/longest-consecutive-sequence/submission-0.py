class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        count = 0
        right = 1
        max_count = 0

        while right < len(nums):
            if nums[right] - nums[left] == 1:
                count += 1
                max_count = max(max_count,count)
            left += 1
            right += 1
        return max_count + 1        
        