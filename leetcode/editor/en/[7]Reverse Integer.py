# Given a signed 32-bit integer x, return x with its digits reversed. If reversi
# ng x causes the value to go outside the signed 32-bit integer range [-231, 231 -
#  1], then return 0. 
# 
#  Assume the environment does not allow you to store 64-bit integers (signed or
#  unsigned). 
# 
#  
#  Example 1: 
#  Input: x = 123
# Output: 321
#  Example 2: 
#  Input: x = -123
# Output: -321
#  Example 3: 
#  Input: x = 120
# Output: 21
#  Example 4: 
#  Input: x = 0
# Output: 0
#  
#  
#  Constraints: 
# 
#  
#  -231 <= x <= 231 - 1 
#  
#  Related Topics Math 
#  👍 4514 👎 6916


# leetcode submit region begin(Prohibit modification and deletion)
from itertools import zip_longest
class Solution:
    def reverse(self, x: int) -> int:
        max_num = [2, 1, 4, 7, 4, 8, 3, 6, 4, 8]
        neg = abs(x) != x
        x = abs(x)
        sum = 0
        digits = []
        while x >= 10:
            if x//10 == x:
                x = x//10
                digit = 0
            else:
                x, digit = divmod(x, 10)
            digits.insert(0, digit)
        digits.insert(0, x)
        # Are we bigger than max_num?
        for d1, d2 in zip(max_num,(len(max_num) - len(digits)) * [0] + list(reversed(digits))):
            if d2 > d1:
                return 0
            elif d2 == d1:
                continue
            else:
                break
        for power, digit in enumerate(digits):
            sum += digit * 10 ** power
        if neg:
            sum *= -1
        return sum

s = Solution()
res = s.reverse(102)
print(res)
res = s.reverse(1534236469)
print(res)
res = s.reverse(-10)
print(res)

# Success:
# Runtime:28 ms, faster than 89.32% of Python3 online submissions.
# Memory Usage:14.3 MB, less than 42.76% of Python3 online submissions.

# leetcode submit region end(Prohibit modification and deletion)
