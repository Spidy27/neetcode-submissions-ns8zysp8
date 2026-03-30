class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = [] # result variable starts null
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # Four Directions to Go
        steps = [len(matrix[0]), len(matrix) - 1] # Suppose for a 3x3 Matrix - steps are [3,2] -> Like step[0] and step[1] will give the detail on moves left in Horizontal and Vertical directions

        r, c, d = 0, -1, 0 # Row, Column and Direction variables are initialized
        # We start just outside the matrix such that the first move goes to [0,0]
        # Direction index is 0, so we start from right direction
        while steps[d & 1]:
            for i in range(steps[d & 1]):
                r += directions[d][0]
                c += directions[d][1]
                res.append(matrix[r][c])
            steps[d & 1] -= 1
            d += 1
            d %= 4
        return res