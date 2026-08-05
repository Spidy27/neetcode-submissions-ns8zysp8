class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        r = 0
        c = 0
        ans = []
        res = []

        while r < len(triplets) and c < len(triplets[0]):
            ans.append(triplets[r][c])

            if r == len(triplets) - 1:
                r = -1
                c += 1
                res.append(max(ans))
                ans = []
            r += 1

        return res == target       


            