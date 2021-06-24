# Given a sorted array of distinct integers and a target value, return the index
#  if the target is found. If not, return the index where it would be if it were i
# nserted in order. 
# 
#  You must write an algorithm with O(log n) runtime complexity. 
# 
#  
#  Example 1: 
#  Input: nums = [1,3,5,6], target = 5
# Output: 2
#  Example 2: 
#  Input: nums = [1,3,5,6], target = 2
# Output: 1
#  Example 3: 
#  Input: nums = [1,3,5,6], target = 7
# Output: 4
#  Example 4: 
#  Input: nums = [1,3,5,6], target = 0
# Output: 0
#  Example 5: 
#  Input: nums = [1], target = 0
# Output: 0
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 104 
#  -104 <= nums[i] <= 104 
#  nums contains distinct values sorted in ascending order. 
#  -104 <= target <= 104 
#  
#  Related Topics Array Binary Search 
#  👍 3761 👎 300


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
from math import ceil
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        window = [0, len(nums)]
        while True:
            look_at = window[0] + (window[1] - window[0]) // 2
            # print(window, look_at)
            val = nums[look_at]
            if val == target:
                return look_at

            if look_at == window[0]:
                if target > val:
                    return look_at + 1
                return look_at
            if look_at == window[1]:
                return look_at+1

            # Adjust window
            if target < val:
                window[1] = look_at
            else:  # target > val
                window[0] = look_at


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
i = 2
res = s.searchInsert([1, 3, 5, 6], i)
print(i, res)
for i in range(8):
    res = s.searchInsert([1, 3, 5, 6], i)
    print(i, res)

# Success:
# Runtime:40 ms, faster than 97.85% of Python3 online submissions.
# Memory Usage:15 MB, less than 52.45% of Python3 online submissions.
# Takeaway