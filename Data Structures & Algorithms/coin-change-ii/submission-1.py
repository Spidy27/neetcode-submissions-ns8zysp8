class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        count = 0
        def dfs(i, stack, total):
            nonlocal count
            if total == amount:
                count += 1
                return

            if i >= len(coins) or total > amount:
                return

            stack.append(coins[i])
            dfs(i, stack, total + coins[i])

            stack.pop()
            dfs(i+1, stack, total)

        dfs(0, [], 0)
        return count            
        