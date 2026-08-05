class Solution:
    def rob(self, nums: List[int]) -> int:
        odd_sum = even_sum = 0
        for i in range(len(nums)):
            if i % 2 != 0:
                odd_sum += nums[i]
            else:
                even_sum += nums[i]
        return max(odd_sum, even_sum)            
        