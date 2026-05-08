class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(temp, remaining):
            if not remaining:
                res.append(temp[:])

            for i in range(len(remaining)):
                temp.append(remaining[i])
                dfs(temp, remaining[:i] + remaining[i+1:])
                temp.pop()

        dfs([], nums)
        return res
                    