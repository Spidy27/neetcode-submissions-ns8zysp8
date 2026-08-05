class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        left = 0
        right = len(nums)-1

        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[right] + nums[left] < target:
                left += 1
            else:
                res.append(left)
                res.append(right)
                break
        return res
            