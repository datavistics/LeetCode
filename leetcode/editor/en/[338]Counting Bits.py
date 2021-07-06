# Given an integer n, return an array ans of length n + 1 such that for each i (
# 0 <= i <= n), ans[i] is the number of 1's in the binary representation of i. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
#  
# 
#  Example 2: 
# 
#  
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= n <= 105 
#  
# 
#  
#  Follow up: 
# 
#  
#  It is very easy to come up with a solution with a runtime of O(n log n). Can 
# you do it in linear time O(n) and possibly in a single pass? 
#  Can you do it without using any built-in function (i.e., like __builtin_popco
# unt in C++)? 
#  
#  Related Topics Dynamic Programming Bit Manipulation 
#  👍 4339 👎 225

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [None] * (n + 1)

        def cb(i, arr):
            if i < 2:
                arr[i] = i
            if i & 1:
                arr[i] = arr[i-1] + 1
            else:
                arr[i] = arr[i//2]
            return arr
        for num in range(n + 1):
            arr = cb(num, arr)
        return arr

# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
res = s.countBits(5)
print(res)

# Success:
# Runtime:88 ms, faster than 58.68% of Python3 online submissions.
# Memory Usage:20.9 MB, less than 35.25% of Python3 online submissions.

