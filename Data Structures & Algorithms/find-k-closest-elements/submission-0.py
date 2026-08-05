class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        closest = {}
        for num in nums:
            closest[num] = abs(x - num)

        res = sorted(closest.items(), key= lambda x: x[1])
        ans = []
        for close in res:
            key, near = close
            ans.append(key)

            if len(ans) == k:
                break
        
        return sorted(ans)            
        