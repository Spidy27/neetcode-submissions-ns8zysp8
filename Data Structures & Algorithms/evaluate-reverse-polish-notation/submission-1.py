class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            try:
                stack.append(int(token))
            except ValueError:

                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    stack.append(a+b)

                if token == '-':
                    stack.append(a-b)

                if token == '*':
                    stack.append(a*b)

                if token == '/':
                    stack.append(int(a / b))

        return stack[-1]                            
        