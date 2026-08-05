class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = []
        for i in range(1, n+1):
            nums.append(i)

        res = []
        def backtrack(temp, remaining):
            nonlocal res
            if len(temp) == k and temp not in res and sorted(temp) not in res:
                res.append(temp[:])

            for i in range(len(remaining)):
                temp.append(remaining[i])
                backtrack(temp, remaining[:i] + remaining[i+1:])
                temp.pop()

        backtrack([], nums)
        return res                
        