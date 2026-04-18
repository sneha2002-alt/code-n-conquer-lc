#  LeetCode 3783: Mirror Distance of an Integer asks you to return the absolute difference between a positive integer n and its mirror (digit reversal, ignoring leading zeros in the reverse)

class Solution:
    def mirrorDistance(self, n: int) -> int:
        reversed_num = 0
        temp = n
        while temp > 0:
            digit = temp % 10
            reversed_num = reversed_num * 10 + digit
            temp //= 10
        return abs(n - reversed_num)



# Test cases
solution = Solution()
print(solution.mirrorDistance(25))  # 27
print(solution.mirrorDistance(10))  # 9
print(solution.mirrorDistance(7))   # 0
print(solution.mirrorDistance(100)) # 99        