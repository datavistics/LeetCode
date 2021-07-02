# Given an integer array nums, find the contiguous subarray (containing at least
#  one number) which has the largest sum and return its sum. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1]
# Output: 1
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [5,4,-1,7,8]
# Output: 23
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 3 * 104 
#  -105 <= nums[i] <= 105 
#  
# 
#  
# Follow up: If you have figured out the O(n) solution, try coding another solut
# ion using the divide and conquer approach, which is more subtle. Related Topics 
# Array Divide and Conquer Dynamic Programming 
#  👍 12629 👎 607

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = nums[0]
        cur_subarray = max_subarray
        for num in nums[1:]:
            cur_subarray = max(num, cur_subarray + num)
            max_subarray = max(max_subarray, cur_subarray)
        return max_subarray


# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
res = s.maxSubArray([5, 4, -1, 7, 8])
print(res)

# Success:
# Runtime:64 ms, faster than 77.05% of Python3 online submissions.
# Memory Usage:15.1 MB, less than 16.70% of Python3 online submissions.