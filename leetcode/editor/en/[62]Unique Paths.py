# A robot is located at the top-left corner of a m x n grid (marked 'Start' in t
# he diagram below). 
# 
#  The robot can only move either down or right at any point in time. The robot 
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in the d
# iagram below). 
# 
#  How many possible unique paths are there? 
# 
#  
#  Example 1: 
# 
#  
# Input: m = 3, n = 7
# Output: 28
#  
# 
#  Example 2: 
# 
#  
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-righ
# t corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
#  
# 
#  Example 3: 
# 
#  
# Input: m = 7, n = 3
# Output: 28
#  
# 
#  Example 4: 
# 
#  
# Input: m = 3, n = 3
# Output: 6
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= m, n <= 100 
#  It's guaranteed that the answer will be less than or equal to 2 * 109. 
#  
#  Related Topics Math Dynamic Programming Combinatorics 
#  👍 5594 👎 250


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # def factorial(n):
        #     res = 1
        #     for i in range(1,n+1):
        #         res *= i
        #     return res
        #
        # return factorial(m + n - 2) // (factorial(m - 1) * factorial(n - 1))

        table = [[None]*n for _ in range(m)]

        def up(m, n):
            if not m or not n:
                return 1
            res = table[m-1][n-1]
            if not res:
                res = up(m - 1, n) + up(m, n - 1)
                table[m-1][n-1] = res
            return res

        res = up(m-1, n-1)
        return res

    # leetcode submit region end(Prohibit modification and deletion)


s = Solution()
res = s.uniquePaths(7, 3)
print(res)

# Success:
# Runtime:24 ms, faster than 96.35% of Python3 online submissions.
# Memory Usage:14.1 MB, less than 85.06% of Python3 online submissions.

# Tabulation
# Success:
# Runtime:32 ms, faster than 65.88% of Python3 online submissions.
# Memory Usage:14.2 MB, less than 85.06% of Python3 online submissions.

# Memoization
# Success:
# Runtime:32 ms, faster than 65.88% of Python3 online submissions.
# Memory Usage:14.5 MB, less than 14.22% of Python3 online submissions.