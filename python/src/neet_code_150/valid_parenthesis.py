class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        if len(s) % 2 == 1:
            return False
        
        stack = []
        for c in s:
            if c in ['[', '(', '{']:
                stack.append(c)
            else:
                match c:
                    case ')':
                        if not stack or stack[-1] != '(':
                            return False
                    case ']':
                        if not stack or stack[-1] != '[':
                            return False
                    case '}':
                        if not stack or stack[-1] != '{':
                            return False
                stack.pop()
        
        return len(stack) == 0
    
s = Solution()

print(s.isValid("([{}])"))
print(s.isValid("([{})"))
print(s.isValid(""))
print(s.isValid("[]"))
print(s.isValid("[]()"))