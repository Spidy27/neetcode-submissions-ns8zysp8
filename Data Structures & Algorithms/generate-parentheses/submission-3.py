class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(open_count, closed_count, current_string):
            # Base case: If the string is complete (length is 2 * n)
            if len(current_string) == n * 2:
                res.append(current_string)
                return
            
            # If we can still add opening parentheses, branch out and add one
            if open_count < n:
                backtrack(open_count + 1, closed_count, current_string + "(")
                
            # If we have more opening than closing, we can safely add a closing parenthesis
            if closed_count < open_count:
                backtrack(open_count, closed_count + 1, current_string + ")")
                
        # Start the recursion with 0 open, 0 closed, and an empty string
        backtrack(0, 0, "")
        
        return res
        