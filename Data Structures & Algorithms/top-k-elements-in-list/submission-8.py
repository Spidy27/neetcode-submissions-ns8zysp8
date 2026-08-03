class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        sorted_freq = sorted(freq.items(), key= lambda x: -x[1])    
        res = []
        count = 0
        for key, value in sorted_freq:
            res.append(key)
            count += 1

            if count == k:
                break

        return res
        