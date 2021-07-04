# Implement strStr(). 
# 
#  Return the index of the first occurrence of needle in haystack, or -1 if need
# le is not part of haystack. 
# 
#  Clarification: 
# 
#  What should we return when needle is an empty string? This is a great questio
# n to ask during an interview. 
# 
#  For the purpose of this problem, we will return 0 when needle is an empty str
# ing. This is consistent to C's strstr() and Java's indexOf(). 
# 
#  
#  Example 1: 
#  Input: haystack = "hello", needle = "ll"
# Output: 2
#  Example 2: 
#  Input: haystack = "aaaaa", needle = "bba"
# Output: -1
#  Example 3: 
#  Input: haystack = "", needle = ""
# Output: 0
#  
#  
#  Constraints: 
# 
#  
#  0 <= haystack.length, needle.length <= 5 * 104 
#  haystack and needle consist of only lower-case English characters. 
#  
#  Related Topics Two Pointers String String Matching 
#  👍 2571 👎 2502


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
res = s.strStr("test", 'bl')
print(res)
res = s.strStr("mississippi", 'issip')
print(res)

# Success:
# Runtime:52 ms, faster than 13.89% of Python3 online submissions.
# Memory Usage:14.4 MB, less than 77.86% of Python3 online submissions.