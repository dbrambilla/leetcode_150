class Solution:
    def isPalindrome(self, s: str) -> bool:
        left: int = 0
        right: int = len(s) - 1

        while left < right:
            left_char = s[left].lower()
            right_char = s[right].lower()

            while left < right and not left_char.isalnum():
                left += 1
                left_char = s[left].lower()

            while left < right and not right_char.isalnum():
                right -= 1
                right_char = s[right].lower()   
            
            if left < right and left_char != right_char:
                return False
            left += 1
            right -= 1
        return True
    
    # write some test cases to validate the solution
def test_is_palindrome():
    solution = Solution()

    # Test case 1: Simple palindrome
    assert solution.isPalindrome("A man, a plan, a canal: Panama") == True

    # Test case 2: Not a palindrome
    assert solution.isPalindrome("race a car") == False

    # Test case 3: Empty string
    assert solution.isPalindrome("") == True

    # Test case 4: Single character
    assert solution.isPalindrome("a") == True

    # Test case 5: Palindrome with special characters
    assert solution.isPalindrome("No 'x' in Nixon") == True

    print("All test cases passed!")

# Run the test cases
test_is_palindrome()