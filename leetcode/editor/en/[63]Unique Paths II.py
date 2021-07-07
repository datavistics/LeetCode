# A robot is located at the top-left corner of a m x n grid (marked 'Start' in t
# he diagram below). 
# 
#  The robot can only move either down or right at any point in time. The robot 
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in the d
# iagram below). 
# 
#  Now consider if some obstacles are added to the grids. How many unique paths 
# would there be? 
# 
#  An obstacle and space is marked as 1 and 0 respectively in the grid. 
# 
#  
#  Example 1: 
# 
#  
# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
#  
# 
#  Example 2: 
# 
#  
# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  m == obstacleGrid.length 
#  n == obstacleGrid[i].length 
#  1 <= m, n <= 100 
#  obstacleGrid[i][j] is 0 or 1. 
#  
#  Related Topics Array Dynamic Programming Matrix 
#  👍 3149 👎 305

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r,c = len(obstacleGrid), len(obstacleGrid[0])
        obstacleGrid[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1,r):
                obstacleGrid[i][0] = obstacleGrid[i-1][0] * (1 - obstacleGrid[i][0])
        for j in range(1,c):
            obstacleGrid[0][j] = obstacleGrid[0][j-1] * (1 - obstacleGrid[0][j])
        for i in range(1, r):
            for j in range(1, c):
                obstacleGrid[i][j] = (obstacleGrid[i][j - 1] + obstacleGrid[i - 1][j]) * (1 - obstacleGrid[i][j])
        return obstacleGrid[-1][-1]


# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
res = s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
# res = s.uniquePathsWithObstacles([[0,1],[0,0]])
print(res)

# Success:
# Runtime:80 ms, faster than 5.38% of Python3 online submissions.
# Memory Usage:14.3 MB, less than 81.71% of Python3 online submissions.
