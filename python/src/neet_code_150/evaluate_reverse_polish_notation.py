from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        i: int = 0
        
        while i < len(tokens):
            e: str = tokens[i]
            if e in ["+","-","*","/"]:
                v2 = s.pop()
                v1 = s.pop()
                match e:
                    case "+":
                        s.append(v1 + v2)
                    case "-":
                        s.append(v1 - v2)
                    case "*":
                        s.append(v1 * v2)
                    case "/":
                        s.append(int(v1 / v2))
            else:
                d: int = int(e)
                s.append(d)
            i += 1
        return s.pop()
    
s = Solution()

print(s.evalRPN(tokens = ["1","2","+","3","*","4","-"]))