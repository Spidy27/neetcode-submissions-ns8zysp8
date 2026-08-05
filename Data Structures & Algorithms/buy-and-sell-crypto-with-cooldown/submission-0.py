class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        def dfs(idx, buying):
            if idx >= len(prices):
                return 0

            cooldown = dfs(idx+1, buying)
            if buying:
                buy = dfs(idx + 1, not buying) - prices[idx]
                return max(buy, cooldown)

            else:
                sell = dfs(idx+2, not buying) + prices[idx]
                return max(sell, cooldown)

        return dfs(0, True)                


        