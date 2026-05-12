class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for i in range(k+1):
            temp_price = prices.copy()
            for source, destination, price in flights:
                if prices[source] == float('inf'):
                    continue

                if prices[source] + price < temp_price[destination]:
                    temp_price[destination] = prices[source] + price  

            prices = temp_price

        if prices[dst] == float('inf'):
            return -1

        return prices[dst]                  
        