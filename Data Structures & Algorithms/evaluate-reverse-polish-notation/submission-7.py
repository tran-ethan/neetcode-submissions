class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for t in tokens:
            if t in ('+', '-', '*', '/'):
                operand2 = stack.pop()
                operand1 = stack.pop()
                expression = f"{operand1} {t} {operand2}"
                result = int(eval(expression))
                stack.append(result)
            else:
                stack.append(int(t))

        return stack.pop()