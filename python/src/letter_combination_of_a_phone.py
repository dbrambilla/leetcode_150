from typing import List

DIGIT_TO_CHARS_MAP = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result: List[str] = []

        def bt(index: int, current: str):
            if index == len(digits):
                result.append(current)
                return
            
            next_char = digits[index]

            for c in DIGIT_TO_CHARS_MAP[next_char]:
                bt(index + 1, current + c)

        bt(0, "")
        return result
    
s = Solution()

print(s.letterCombinations("23"))