// LeetCode 0009: Palindrome Number
// Difficulty: Easy

// Given an integer x, return true if x is palindrome integer.

// An integer is a palindrome when it reads the same backward as forward. For example, 121 is a palindrome while 123 is not.

let isPalindrome = (x) => {
    let pal_str = String(x)
    let rev = pal_str.split('').reverse().join('')
    if (pal_str == rev) {
        return true
    } else {
        return false
    }
}