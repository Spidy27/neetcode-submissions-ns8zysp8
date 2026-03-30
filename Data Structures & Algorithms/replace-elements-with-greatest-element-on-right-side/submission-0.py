class Solution:
    def replaceElements(self, nums: List[int]) -> List[int]:
        left = 1
        res = []

        while left < len(nums):
            max_index = nums.index(max(nums[left:]))
            res.append(nums[max_index])
            left += 1

        res.append(-1)

        return res    
        