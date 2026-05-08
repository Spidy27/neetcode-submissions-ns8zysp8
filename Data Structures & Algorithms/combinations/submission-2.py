class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n+1)]
        res = []
        def help(i, tmp):
            if len(tmp) == k:
                res.append(tmp[:])
                return


            for j in range(i, len(nums)):
                tmp.append(nums[j])
                help(j+1, tmp)
                tmp.pop()

        help(0, [])

        return res