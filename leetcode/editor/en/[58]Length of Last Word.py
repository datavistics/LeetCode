# Given a string s consists of some words separated by spaces, return the length
#  of the last word in the string. If the last word does not exist, return 0. 
# 
#  A word is a maximal substring consisting of non-space characters only. 
# 
#  
#  Example 1: 
#  Input: s = "Hello World"
# Output: 5
#  Example 2: 
#  Input: s = " "
# Output: 0
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 104 
#  s consists of only English letters and spaces ' '. 
#  
#  Related Topics String 
#  👍 1207 👎 3324

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        wl = s.split()
        if wl:
            return len(wl[-1])
        return 0
        # count = 0
        # for let in s[::-1]:
        #     if let != ' ':
        #         count += 1
        #     elif count:
        #         return count
        # return count

# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
res = s.lengthOfLastWord('a b ')
print(res)
res = s.lengthOfLastWord(' ')
print(res)
res = s.lengthOfLastWord('Hello World')
print(res)

# Success:
# Runtime:32 ms, faster than 55.53% of Python3 online submissions.
# Memory Usage:14.3 MB, less than 64.27% of Python3 online submissions.