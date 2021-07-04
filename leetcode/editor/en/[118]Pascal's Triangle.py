# Given an integer numRows, return the first numRows of Pascal's triangle. 
# 
#  In Pascal's triangle, each number is the sum of the two numbers directly abov
# e it as shown: 
# 
#  
#  Example 1: 
#  Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#  Example 2: 
#  Input: numRows = 1
# Output: [[1]]
#  
#  
#  Constraints: 
# 
#  
#  1 <= numRows <= 30 
#  
#  Related Topics Array Dynamic Programming 
#  👍 2942 👎 140

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        def gen(prev_row):
            temp = [0,*prev_row, 0]
            next_row = []
            for i,j in zip(temp[:-1], temp[1:]):
                next_row.append(i+j)
            return next_row
        out = [[1]] + [None] * (numRows - 1)
        for i in range(1, numRows):
            out[i] = gen(out[i-1])
        return out

# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
res = s.generate(3)
print(res)

# Success:
# Runtime:24 ms, faster than 95.44% of Python3 online submissions.
# Memory Usage:14.5 MB, less than 23.81% of Python3 online submissions.
# Time:: 00:06:06