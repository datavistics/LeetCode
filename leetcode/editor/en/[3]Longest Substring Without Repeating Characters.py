# Given a string s, find the length of the longest substring without repeating c
# haracters. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a 
# substring.
#  
# 
#  Example 4: 
# 
#  
# Input: s = ""
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= s.length <= 5 * 104 
#  s consists of English letters, digits, symbols and spaces. 
#  
#  Related Topics Hash Table String Sliding Window 
#  👍 15681 👎 778


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        d = {}
        left = 0
        longest = 0
        for right, letter in enumerate(s):
            if letter in d and left <= d[letter]:
                # This is for when there are repeats that are adjacent
                left = d[letter] + 1
                    # print(s[left:right])
            d[letter] = right
            # print(s[left:right])
            if longest < right - left:
                longest = right - left
        return longest + 1


# leetcode submit region end(Prohibit modification and deletion)

# s = Solution.lengthOfLongestSubstring(None, "bbbbbb")
s = Solution.lengthOfLongestSubstring(None, "abba")
# s = Solution.lengthOfLongestSubstring(None, "abcabcbb")
# s = Solution.lengthOfLongestSubstring(None, "nfpdmpi")
print(s)

# Success:
# Runtime: 44 ms, faster than 98.82% of Python3 online submissions.
# Memory Usage: 14.1 MB, less than 98.92% of Python3 online submissions.
