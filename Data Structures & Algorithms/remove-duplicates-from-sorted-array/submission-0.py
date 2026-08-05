class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 1
        res = nums

        while right < len(res):
            if res[left] == res[right]:
                del res[right]

            right += 1
            left += 1

        if res[-1] == res[-2]:
            del res[-1]

        return len(res)            
        