class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for t in tokens:
            if t == '+':
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = operand1 + operand2
                stack.append(result)
            elif t == '-':
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = operand1 - operand2
                stack.append(result)
            elif t == '*':
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = operand1 * operand2
                stack.append(result)
            elif t == '/':
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = int(operand1 / operand2)
                stack.append(result)
            else:
                stack.append(int(t))

        return stack.pop()