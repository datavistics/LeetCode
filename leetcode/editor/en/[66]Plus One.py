# Given a non-empty array of decimal digits representing a non-negative integer,
#  increment one to the integer. 
# 
#  The digits are stored such that the most significant digit is at the head of 
# the list, and each element in the array contains a single digit. 
# 
#  You may assume the integer does not contain any leading zero, except the numb
# er 0 itself. 
# 
#  
#  Example 1: 
# 
#  
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
#  
# 
#  Example 2: 
# 
#  
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
#  
# 
#  Example 3: 
# 
#  
# Input: digits = [0]
# Output: [1]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= digits.length <= 100 
#  0 <= digits[i] <= 9 
#  
#  Related Topics Array Math 
#  👍 2501 👎 3344

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        remainder = 1
        while True:
            sum = digits[i] + remainder
            remainder = sum // 10

            digits[i] = sum - remainder * 10
            if not remainder:
                return digits
            else:
                i -= 1
                if i < 0:
                    return [remainder] + digits


# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
res = s.plusOne([1, 9])
print(res)

# Success:
# Runtime:28 ms, faster than 89.03% of Python3 online submissions.
# Memory Usage:14 MB, less than 90.53% of Python3 online submissions.