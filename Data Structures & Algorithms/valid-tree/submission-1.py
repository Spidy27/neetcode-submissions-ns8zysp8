class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                return find(parent[x])
            return x

        def union(x,y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            parent[rx] = ry
            return True

        for x, y in edges:
            if not union(x, y):
                return False

        return len(edges) == n - 1                        
        