class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        left = 0
        right = 1
        alien = {}

        while right < len(words):
            for i in range(min(len(words[left]), len(words[right]))):
                if words[left][i] != words[right][i]:
                    alien[words[left][i]] = words[right][i]

            left += 1
            right += 1

        ans = []
        length = 0
        maximum = 0

        def dfs(key):
            nonlocal res
            if alien.get(key) is None:
                res.append(key)
                return

            res.append(key)
            dfs(alien[key])

        for key, value in alien.items():
            res = []
            dfs(key)
            length = len(res)
            maximum = max(maximum, length)
            ans.append("".join(res))

        for word in ans:
            if len(word) == maximum:
                return word

        return -1                                
        