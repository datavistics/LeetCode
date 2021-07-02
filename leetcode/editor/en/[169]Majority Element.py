# Given an array nums of size n, return the majority element. 
# 
#  The majority element is the element that appears more than ⌊n / 2⌋ times. You
#  may assume that the majority element always exists in the array. 
# 
#  
#  Example 1: 
#  Input: nums = [3,2,3]
# Output: 3
#  Example 2: 
#  Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#  
#  
#  Constraints: 
# 
#  
#  n == nums.length 
#  1 <= n <= 5 * 104 
#  -231 <= nums[i] <= 231 - 1 
#  
# 
#  
# Follow-up: Could you solve the problem in linear time and in O(1) space? Relat
# ed Topics Array Hash Table Divide and Conquer Sorting Counting 
#  👍 5563 👎 270

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        max_count = 0
        max_el = None
        for el in nums:
            new_count = 1 + d.get(el, 0)
            d[el] = new_count
            if new_count > max_count:
                max_el = el
                max_count = new_count
        return max_el
# leetcode submit region end(Prohibit modification and deletion)

# Success:
# Runtime:188 ms, faster than 20.58% of Python3 online submissions.
# Memory Usage:15.6 MB, less than 9.87% of Python3 online submissions