class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = []
        for query in queries:
            min_length = float('inf')
            for interval in intervals:
                start, end = interval
                
                if query in interval:
                    length = end - start + 1
                    min_length = min(min_length, length)
            if min_length == float('inf'):
                res.append(-1)
            else:
                res.append(min_length)    

        return res            
