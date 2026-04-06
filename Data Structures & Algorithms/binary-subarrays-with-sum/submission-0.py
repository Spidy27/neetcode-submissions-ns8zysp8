class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        prefix = 0

        count = [0] * (n+1)
        count[0] = 1
        res = 0

        for num in nums:
            prefix += num
            if prefix >= goal:
                res += count[prefix - goal]

            count[prefix] += 1

        return res
                
        