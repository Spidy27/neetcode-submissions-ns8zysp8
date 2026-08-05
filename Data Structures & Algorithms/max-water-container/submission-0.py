class Solution:
    def maxArea(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        max_area = 0

        while left != right:
            area = min(nums[left],nums[right]) * (right - left)
            max_area = max(max_area,area)
            left += 1

        return max_area   
        