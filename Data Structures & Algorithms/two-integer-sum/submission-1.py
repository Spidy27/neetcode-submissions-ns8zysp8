class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_nums = [abs(n) for n in nums]
        new_target = abs(target)
        res = []
        left = 0
        right = len(new_nums)-1

        while left < right:
            if new_nums[left] + new_nums[right] > new_target:
                right -= 1
            elif new_nums[right] + new_nums[left] < new_target:
                left += 1
            else:
                res.append(left)
                res.append(right)
                break
        return res
            