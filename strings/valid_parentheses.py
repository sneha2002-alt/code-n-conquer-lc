# Problem-20: Valid Parentheses
#  Problem Statement:
# Given a string s containing just the characters 
# '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

# A string is valid if:
# 1. Open brackets are closed by the same type
# 2. Open brackets are closed in correct order
# 3. Every closing bracket has a corresponding opening bracket

# Approach: Stack
# We use a stack (LIFO) to track opening brackets.

# Steps:
# 1. Traverse each character in string
# 2. If opening bracket → push to stack
# 3. If closing bracket:
#    - Pop from stack
#    - Check if it matches
# 4. If mismatch → return False
# 5. At end, stack must be empty

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
  def isValid(self, s: str) -> bool:
    stack = []

    mapping = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

    for char in s:
      if char in mapping:
        top = stack.pop() if stack else '#'
        if mapping[char] != top:
          return False
      else:
        stack.append(char)

    return len(stack) == 0
      
# for local testing 
if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [
        "()",
        "()[]{}",
        "(]",
        "([)]",
        "{[]}",
        "",
        "((()))"
    ]
    
    for s in test_cases:
        print(f"Input: {s} -> Output: {sol.isValid(s)}")      