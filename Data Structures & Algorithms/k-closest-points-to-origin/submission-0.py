class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            x, y = point
            distance = math.sqrt(x**2 + y**2)
            distances.append(distance)

        res = sorted(range(len(distances)), key= lambda i: distances[i])
        k_indices = res[:k]

        return [points[i] for i in k_indices]    
        