# Given an array of integers nums and an integer target, return indices of the t
# wo numbers such that they add up to target. 
# 
#  You may assume that each input would have exactly one solution, and you may n
# ot use the same element twice. 
# 
#  You can return the answer in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [3,3], target = 6
# Output: [0,1]
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= nums.length <= 103 
#  -109 <= nums[i] <= 109 
#  -109 <= target <= 109 
#  Only one valid answer exists. 
#  
#  Related Topics Array Hash Table 
#  👍 20051 👎 706

from typing import List
import bisect
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # Create dict of differences
        # d = {target - k: i for i, k in enumerate(nums)}
        #
        # # Return difference indices
        # for i, k in enumerate(nums):
        #     v = d.get(k)
        #     if v is not None and v != i:
        #         if i < v:
        #             return [i,v]
        #         else:
        #             return [v,i]
        temp = sorted(nums.copy())
        for i, num in enumerate(temp):
            bis = bisect.bisect_left(temp, target - num, lo=i + 1)
            j = bis if bis < len(nums) - 1 else len(nums) - 1
            if num + temp[j] == target:
                look_1 = temp[i]
                look_2 = temp[j]
                out = []
                for i, num in enumerate(nums):
                    if num == look_1:
                        out.append(i)
                        if len(out) == 2:
                            return out
                        else:
                            continue
                    if num == look_2:
                        out.append(i)
                        if len(out) == 2:
                            return out
                        else:
                            continue
                return out

# leetcode submit region end(Prohibit modification and deletion)


# s = Solution.twoSum(None,[3,2,4], 6)
s = Solution.twoSum(None,[3,3], 6)
# s = Solution.twoSum(None, [3, 2, 3], 6)
# s = Solution.twoSum(None, [-1, -2, -3, -4, -5], -8)
print(s)

# Success:
# Runtime: 64 ms, faster than 53.38% of Python3 online submissions.
# Memory Usage: 15 MB, less than 61.09% of Python3 online submissions.