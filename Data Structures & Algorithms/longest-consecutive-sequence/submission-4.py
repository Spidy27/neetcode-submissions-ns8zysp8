class Solution:
    def longestConsecutive(self,nums: list):
        if len(nums) == 0:
            return 0
        nums.sort()
        count = 0
        left = 0
        for right in range(1, len(nums)):
            if nums[left] != nums[right]:  
                diff = nums[right] - nums[left]
                if diff == 1:
                    count += 1 
            left += 1           
        return count + 1
        