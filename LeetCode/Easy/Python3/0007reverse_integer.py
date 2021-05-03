# LeetCode 0007: Reverse Integer
# Difficulty: Easy
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


class Solution:
    def reverse(self, x: int) -> int:
        strNum = str(x)
        if x >= 0:
            revstr = strNum[::-1]
        else: 
            temp = strNum[1:]
            temp2 = temp[::-1]
            revstr = '-' + temp2
        if int(revstr) > 2**31-1 or int(revstr) <= -(2**31):
            return 0
        else:
            return int(revstr)

