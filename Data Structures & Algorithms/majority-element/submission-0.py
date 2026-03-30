class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = {}
        for num in nums:
            res[num] = 1 + res.get(num,0)
        major = 0
        max_freq = 0

        for num,freq in res.items():
            if freq > max_freq:
                max_freq = freq
                major = num

        return major            
        