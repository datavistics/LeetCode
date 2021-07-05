# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal
# 's triangle. 
# 
#  In Pascal's triangle, each number is the sum of the two numbers directly abov
# e it as shown: 
# 
#  
#  Example 1: 
#  Input: rowIndex = 3
# Output: [1,3,3,1]
#  Example 2: 
#  Input: rowIndex = 0
# Output: [1]
#  Example 3: 
#  Input: rowIndex = 1
# Output: [1,1]
#  
#  
#  Constraints: 
# 
#  
#  0 <= rowIndex <= 33 
#  
# 
#  
#  Follow up: Could you optimize your algorithm to use only O(rowIndex) extra sp
# ace? 
#  Related Topics Array Dynamic Programming 
#  👍 1484 👎 229

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def factorial(n):
            out = 1
            for i in range(n):
                out*= i+1
            return out
        def ncr(n, r):
            return factorial(n)//(factorial(r)* factorial(n-r))
        return [ncr(rowIndex,r) for r in range(rowIndex + 1)]

# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
res = s.getRow(3)
print(res)

# Success:
# Runtime:32 ms, faster than 63.37% of Python3 online submissions.
# Memory Usage:14.1 MB, less than 91.98% of Python3 online submissions.
# Time:: 00:10:23