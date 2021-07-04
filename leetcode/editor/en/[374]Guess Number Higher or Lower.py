# We are playing the Guess Game. The game is as follows: 
# 
#  I pick a number from 1 to n. You have to guess which number I picked. 
# 
#  Every time you guess wrong, I will tell you whether the number I picked is hi
# gher or lower than your guess. 
# 
#  You call a pre-defined API int guess(int num), which returns 3 possible resul
# ts: 
# 
#  
#  -1: The number I picked is lower than your guess (i.e. pick < num). 
#  1: The number I picked is higher than your guess (i.e. pick > num). 
#  0: The number I picked is equal to your guess (i.e. pick == num). 
#  
# 
#  Return the number that I picked. 
# 
#  
#  Example 1: 
#  Input: n = 10, pick = 6
# Output: 6
#  Example 2: 
#  Input: n = 1, pick = 1
# Output: 1
#  Example 3: 
#  Input: n = 2, pick = 1
# Output: 1
#  Example 4: 
#  Input: n = 2, pick = 2
# Output: 2
#  
#  
#  Constraints: 
# 
#  
#  1 <= n <= 231 - 1 
#  1 <= pick <= n 
#  
#  Related Topics Binary Search Interactive 
#  👍 674 👎 2154


# leetcode submit region begin(Prohibit modification and deletion)
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            mid = l + (r-l)//2
            g = guess(mid)
            if not g:
                return mid
            elif g < 0:
                r = mid -1
            else:
                l = mid + 1
        return l
        
# leetcode submit region end(Prohibit modification and deletion)

# Success:
# Runtime:32 ms, faster than 50.78% of Python3 online submissions.
# Memory Usage:14.1 MB, less than 71.10% of Python3 online submissions.
# Time:: 00:02:32