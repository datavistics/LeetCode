# Given a non-negative integer x, compute and return the square root of x. 
# 
#  Since the return type is an integer, the decimal digits are truncated, and on
# ly the integer part of the result is returned. 
# 
#  Note: You are not allowed to use any built-in exponent function or operator, 
# such as pow(x, 0.5) or x ** 0.5. 
# 
#  
#  Example 1: 
# 
#  
# Input: x = 4
# Output: 2
#  
# 
#  Example 2: 
# 
#  
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part is
#  truncated, 2 is returned. 
# 
#  
#  Constraints: 
# 
#  
#  0 <= x <= 231 - 1 
#  
#  Related Topics Math Binary Search 
#  👍 2180 👎 2462

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        lo, hi = 0, x
        while True:
            mid = (hi + lo) // 2
            if x < mid ** 2:
                hi = mid
            else:
                lo = mid
            if hi - lo == 1:
                return lo


# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
res = s.mySqrt(2)
print(res)

# Success:
# Runtime:40 ms, faster than 50.74% of Python3 online submissions.
# Memory Usage:14.2 MB, less than 38.05% of Python3 online submissions.