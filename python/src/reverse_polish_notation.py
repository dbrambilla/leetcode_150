from typing import List
class Solution:
    def isOp(self, s):
        return s in ['+', '-', '/', '*']
    
    def compute(self, v1, v2, op) -> int:
        match op:
            case "+":
                return v1 + v2
            case "-":
                return v1 - v2
            case "*":
                return v1 * v2
            case "/":
                return v1 / v2

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        i: int = len(tokens) - 1

        if len(tokens) == 1:
            return int(tokens[0])

        while i >= 0:
            el = tokens[i]
            if self.isOp(el):
                stack.append(el)
            else:
                if self.isOp(stack[-1]):
                    # If stack has operation append
                    stack.append(int(el))
                else:
                    found = True
                    while found:
                        # If stack has value then pop and the operation and put back
                        v = stack.pop()
                        op = stack.pop()
                        found = not self.isOp(stack[-1]) if stack else False
                        res = self.compute(int(el), v, op)
                        stack.append(int(res))
                        if found:
                            el = stack.pop()
            i -= 1

        if len(stack) == 1:
            res = stack.pop()
        else:
            while stack:
                res = self.compute(stack.pop(), stack.pop(), stack.pop())

        return res



s = Solution()
# print(s.evalRPN(["2","1","+","3","*"]))
# print(s.evalRPN(["4","13","5","/","+"]))
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))