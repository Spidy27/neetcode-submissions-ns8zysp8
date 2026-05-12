class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = {}
        for i, char in enumerate(s):
            freq[char] = i

        res = []
        size = 0
        end = 0
        for i, char in enumerate(s):
            size += 1
            end = max(end, freq[char])

            if end == i:
                res.append(size)
                size = 0

        return res            
        