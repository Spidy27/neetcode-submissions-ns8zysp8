class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        memo = set()

        def dfs(i, stack, total):
            if sum(stack) == 0 and len(stack) == 3 and tuple(sorted(stack)) not in memo:
                res.append(stack[:])
                memo.add(tuple(sorted(stack)))
                return

            if i >= len(nums):
                return

            stack.append(nums[i])
            dfs(i+1, stack, total + nums[i])
            stack.pop()
            dfs(i+1, stack, total)

        dfs(0, [], 0)    
        return res