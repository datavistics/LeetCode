# Given n non-negative integers a1, a2, ..., an , where each represents a point 
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of
#  the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x
# -axis forms a container, such that the container contains the most water. 
# 
#  Notice that you may not slant the container. 
# 
#  
#  Example 1: 
# 
#  
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,
# 3,7]. In this case, the max area of water (blue section) the container can conta
# in is 49.
#  
# 
#  Example 2: 
# 
#  
# Input: height = [1,1]
# Output: 1
#  
# 
#  Example 3: 
# 
#  
# Input: height = [4,3,2,1,4]
# Output: 16
#  
# 
#  Example 4: 
# 
#  
# Input: height = [1,2,1]
# Output: 2
#  
# 
#  
#  Constraints: 
# 
#  
#  n == height.length 
#  2 <= n <= 105 
#  0 <= height[i] <= 104 
#  
#  Related Topics Array Two Pointers Greedy 
#  👍 10323 👎 740

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = min(height[left], height[right]) * (right - left)
        for _ in range(right - 1):
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            max_water = max(max_water, min(height[left], height[right]) * (right - left))
        return max_water


# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
res = s.maxArea([4, 3, 2, 1, 4])
print(res)

# Success:
# Runtime:824 ms, faster than 17.61% of Python3 online submissions.
# Memory Usage:27.5 MB, less than 65.74% of Python3 online submissions.
