# LeetCode 0014: Longest Common Prefix
# Difficulty: Easy

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# STILL IN PROGRESS....
# class Solution(object):
#     def longest

#       if len(strs) == 0:
#          return ""
#       current = strs[0]
#       for i in range(1,len(strs)):
#          temp = ""
#          if len(current) == 0:
#             break
#          for j in range(len(strs[i])):
#             if j<len(current) and current[j] == strs[i][j]:
#                temp+=current[j]
#             else:
#                break
#          current = temp
#       return current
# input_list = ["school","schedule","scotland"]
# ob1 = Solution()
# print(ob1.longestCommonPrefix(input_list))