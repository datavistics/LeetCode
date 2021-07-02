# Write an algorithm to determine if a number n is happy. 
# 
#  A happy number is a number defined by the following process: 
# 
#  
#  Starting with any positive integer, replace the number by the sum of the squa
# res of its digits. 
#  Repeat the process until the number equals 1 (where it will stay), or it loop
# s endlessly in a cycle which does not include 1. 
#  Those numbers for which this process ends in 1 are happy. 
#  
# 
#  Return true if n is a happy number, and false if not. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
#  
# 
#  Example 2: 
# 
#  
# Input: n = 2
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 231 - 1 
#  
#  Related Topics Hash Table Math Two Pointers 
#  👍 3388 👎 546


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_square_sum(n):
            square_sum = 0
            div = n

            while True:
                if not div:
                    break
                div, rem = divmod(div, 10)
                square_sum += rem**2
            return square_sum

        fast = slow = n
        while True:
            slow = get_square_sum(slow)
            fast = get_square_sum(fast)
            fast = get_square_sum(fast)
            if slow == 1 or fast == 1:
                return True
            elif slow == fast:
                return False


# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
res = s.isHappy(7)
print(res)

# Success:
# Runtime:28 ms, faster than 95.13% of Python3 online submissions.
# Memory Usage:14.3 MB, less than 46.20% of Python3 online submissions

# Success:
# Runtime:36 ms, faster than 61.67% of Python3 online submissions.
# Memory Usage:14.5 MB, less than 14.73% of Python3 online submissions.