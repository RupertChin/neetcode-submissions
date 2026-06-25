class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Approach:
        - push numbers into stack
        - when get operator, pop 2 numbers, push result
        """

        stack = []
        operators = {'+', '-', '*', '/'}
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if t == '+':
                    stack.append(num1 + num2)
                elif t == '-':
                    stack.append(num1 - num2)
                elif t == '*':
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num1 / num2))
        
        return int(stack.pop())