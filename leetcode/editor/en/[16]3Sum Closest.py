# Given an array nums of n integers and an integer target, find three integers i
# n nums such that the sum is closest to target. Return the sum of the three integ
# ers. You may assume that each input would have exactly one solution. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#  
# 
#  
#  Constraints: 
# 
#  
#  3 <= nums.length <= 10^3 
#  -10^3 <= nums[i] <= 10^3 
#  -10^4 <= target <= 10^4 
#  
#  Related Topics Array Two Pointers Sorting 
#  👍 3641 👎 183

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 4:
            return sum(nums)
        nums.sort()
        closest = float('inf')

        for i, v_i in enumerate(nums[:-2]):
            if i and v_i == nums[i-1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                int_sum = v_i + nums[j] + nums[k]
                if int_sum < target:
                    j += 1
                elif int_sum > target:
                    k -= 1
                else:
                    return target

                if abs(target - int_sum) < abs(target - closest):
                    closest = int_sum
        return closest


# leetcode submit region end(Prohibit modification and deletion)

s = Solution.threeSumClosest(None, [-3, 2, 1, 0], 1)
print(s)

# Success:
# Runtime: 96 ms, faster than 95.51% of Python3 online submissions.
# Memory Usage: 14.3 MB, less than 69.98% of Python3 online submissions.
