class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i, num in enumerate(nums):
            diff = target - num

            if num not in check:
                check[diff] = (num, i)

            else:
                return [check[num][1], i]    
        
        return -1