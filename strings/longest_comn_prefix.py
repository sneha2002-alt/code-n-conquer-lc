# LeetCode Problem-14 : Longest Common Prefix
# Problem Statement
# Given an array of strings strs, find the longest common prefix among them.
# If there is no common prefix, return an empty string "".

# Algorithm Steps:
# 1.Loop through each character index of the first string.
# 2.Store current character.
# 3.Compare with all other strings at same index.
# 4.If mismatch → return substring till previous index.
# 5.If loop completes → return entire first string.

# TC - O(n x m) where n = number of strings, m = length of shortest string

# SC - O(1)

def longestCommonPrefix(strs):
    for i in range(len(strs[0])):
        char = strs[0][i]
        
        for j in range(1, len(strs)):
            if (i >= len(strs[j])) or (strs[j][i] != char):
                return strs[0][:i]
    
    return strs[0]


# Example usage
lst = ["flower", "flow", "flight"]
print(longestCommonPrefix(lst))  # Output: "fl"
                     