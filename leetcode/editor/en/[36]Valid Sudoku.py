# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be v
# alidated according to the following rules: 
# 
#  
#  Each row must contain the digits 1-9 without repetition. 
#  Each column must contain the digits 1-9 without repetition. 
#  Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 with
# out repetition. 
#  
# 
#  Note: 
# 
#  
#  A Sudoku board (partially filled) could be valid but is not necessarily solva
# ble. 
#  Only the filled cells need to be validated according to the mentioned rules. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being
#  modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is inval
# id.
#  
# 
#  
#  Constraints: 
# 
#  
#  board.length == 9 
#  board[i].length == 9 
#  board[i][j] is a digit or '.'. 
#  
#  Related Topics Array Hash Table Matrix 
#  👍 2838 👎 581

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                if (i, val) in seen or (val, j) in seen or (i // 3, j // 3, val) in seen:
                    return False
                seen.add((i, val))
                seen.add((val, j))
                seen.add((i // 3, j // 3, val))
        return True
        rows


# leetcode submit region end(Prohibit modification and deletion)

from timerit import Timerit

t1 = Timerit(num=200, verbose=2)
# False
b = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

# True
b = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
     [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
     ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
     [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
# False
b =  [[".", ".", "4", ".", ".", ".", "6", "3", "."],
      [".", ".", ".", ".", ".", ".", ".", ".", "."],
      ["5", ".", ".", ".", ".", ".", ".", "9", "."],
      [".", ".", ".", "5", "6", ".", ".", ".", "."],
      ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
      [".", ".", ".", "7", ".", ".", ".", ".", "."],
      [".", ".", ".", "5", ".", ".", ".", ".", "."],
      [".", ".", ".", ".", ".", ".", ".", ".", "."],
      [".", ".", ".", ".", ".", ".", ".", ".", "."]]

for timer in t1:
    with timer:
        s = Solution.isValidSudoku(None, b)
print(s)

# Success:
# Runtime: 156 ms, faster than 8.83% of Python3 online submissions.
# Memory Usage: 13.9 MB, less than 99.79% of Python3 online submissions.
