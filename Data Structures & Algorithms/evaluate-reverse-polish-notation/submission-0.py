class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i not in "+-*/":
                stack.append(int(i))
            elif i == '-':
                second = stack.pop()
                first = stack.pop()
                val = first - second
                stack.append(val)
            elif i == '+':
                second = stack.pop()
                first = stack.pop()
                val = first + second
                stack.append(val)
            elif i == '*':
                second = stack.pop()
                first = stack.pop()
                val = first * second
                stack.append(val)
            elif i == '/':
                second = stack.pop()
                first = stack.pop()
                val = int(first / second)
                stack.append(val)
        return stack[-1]
            