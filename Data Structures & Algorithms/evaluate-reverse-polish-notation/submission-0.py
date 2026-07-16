class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in {"+","-","*","/"}:
                if len(stack) < 2:
                    return False
                elif i == "+":
                    a = stack.pop()
                    b = stack.pop()
                    ans = b + a
                    stack.append(int(ans))
                elif i == "-":
                    a = stack.pop()
                    b = stack.pop()
                    ans = b - a
                    stack.append(int(ans))
                elif i == "*":
                    a = stack.pop()
                    b = stack.pop()
                    ans = b * a
                    stack.append(int(ans))
                elif i == "/":
                    a = stack.pop()
                    b = stack.pop()
                    ans = b / a
                    stack.append(int(ans))
            else: 
                stack.append(int(i))
        return stack.pop()
