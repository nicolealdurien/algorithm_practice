// LeetCode #7: Reverse Integer
// Difficulty: Easy
// Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

// Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

var reverse = function(x) {
    let limit = 2147483647
    let negHold = x < 0 ? -1 : 1
    let str = String(Math.abs(x))
    let newStr = ''
    for (let i = str.length-1; i >= 0; i--) {
        newStr += str[i]
    }
    let revNum = Number(newStr)
    return revNum > limit ? 0 : revNum * negHold
};
