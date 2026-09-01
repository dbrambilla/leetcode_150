class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        stack = []

        for c in s:
            if c in ['[', '(', '{']:
                stack.append(c)
            else:
                match c:
                    case ')':
                        if stack[-1] != '(':
                            return False
                    case ']':
                        if stack[-1] != '[':
                            return False
                    case '}':
                        if stack[-1] != '{':
                            return False
                stack.pop()
        return len(stack) == 0
    
s = Solution()
print(s.isValid("[]"))
print(s.isValid("[](){}"))
print(s.isValid("[}"))