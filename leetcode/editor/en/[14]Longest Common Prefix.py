# Write a function to find the longest common prefix string amongst an array of 
# strings. 
# 
#  If there is no common prefix, return an empty string "". 
# 
#  
#  Example 1: 
# 
#  
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#  
# 
#  Example 2: 
# 
#  
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= strs.length <= 200 
#  0 <= strs[i].length <= 200 
#  strs[i] consists of only lower-case English letters. 
#  
#  Related Topics String 
#  👍 4590 👎 2318

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ''
        comp = strs[0]
        for i in range(len(comp)):
            comp_letter = comp[i]
            for string in strs[1:]:
                if i == len(string) or string[i] != comp_letter:
                    return pre
            pre += comp_letter
        return pre


# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
res = s.longestCommonPrefix(['', ''])
# res = s.longestCommonPrefix(["flower","flow","flight", ''])
print(res)

# Success:
# Runtime:36 ms, faster than 56.77% of Python3 online submissions.
# Memory Usage:14.4 MB, less than 54.08% of Python3 online submissions.
# Time:: 00:09:23