class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) != 1:
            stones.sort()
            n = len(stones) - 1
            diff = stones[n] - stones[n-1]
            stones.remove(stones[n])
            stones.remove(stones[n-1])
            stones.append(diff)

        return stones[0]    
        