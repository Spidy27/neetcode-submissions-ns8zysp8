class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token.isdigit():
                stack.append(token)

            else:
                b = int(stack.pop())
                a = int(stack.pop())

                if token == '+':
                    stack.append(a+b)

                if token == '-':
                    stack.append(a-b)

                if token == '*':
                    stack.append(a*b)

                if token == '/':
                    stack.append(a // b)

        return stack[-1]                            
        