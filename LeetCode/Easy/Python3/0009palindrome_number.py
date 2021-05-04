# LeetCode 0009: Palindrome Number
# Difficulty: Easy

# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward. For example, 121 is a palindrome while 123 is not.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        pal_str = str(x)
        rev = pal_str[::-1]
        if pal_str == rev:
            return True
        else:
            return False