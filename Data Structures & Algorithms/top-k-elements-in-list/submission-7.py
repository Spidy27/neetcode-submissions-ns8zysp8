class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        res = sorted(freq.items(),key= lambda x: x[-1], reverse= True) 
        count = 0
        ans = []

        for key, value in res:
            ans.append(key)
            count += 1

            if count == k:
                return ans

        return -1        

        