# LeetCode 28 - Find the Index of the First Occurrence in a String
# Difficulty: Easy
# Approach: Sliding Window
# Time Complexity: O(n * m)
# Space Complexity: O(1)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        
        for i in range(n - m + 1):
            if haystack[i : i + m] == needle:
                return i
        
        return -1


# ---- Test Cases ----
solution = Solution()

print(solution.strStr("sadbutsad", "sad"))   # Expected: 0
print(solution.strStr("leetcode", "leeto"))  # Expected: -1
print(solution.strStr("hello", "ll"))        # Expected: 2
print(solution.strStr("a", "a"))             # Expected: 0
print(solution.strStr("abc", "c"))           # Expected: 2

    
