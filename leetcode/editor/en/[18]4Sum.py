# Given an array nums of n integers, return an array of all the unique quadruple
# ts [nums[a], nums[b], nums[c], nums[d]] such that: 
# 
#  
#  0 <= a, b, c, d < n 
#  a, b, c, and d are distinct. 
#  nums[a] + nums[b] + nums[c] + nums[d] == target 
#  
# 
#  You may return the answer in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 200 
#  -109 <= nums[i] <= 109 
#  -109 <= target <= 109 
#  
#  Related Topics Array Two Pointers Sorting 
#  👍 3726 👎 446

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        nums.sort()

        for i, v_i in enumerate(nums[:-3]):
            if i and v_i == nums[i - 1]:
                continue
            prev_v_j = None
            for j, v_j in enumerate(nums[i + 1:-2], start=i + 1):
                if prev_v_j == v_j:
                    continue
                prev_v_j = v_j
                k = j + 1
                l = len(nums) - 1
                while k < l:
                    v_k, v_l = nums[k], nums[l]
                    s = v_i + v_j + v_k + v_l
                    if s < target:
                        k += 1
                    elif s > target:
                        l -= 1
                    else:
                        yield (v_i, v_j, nums[k], nums[l])

                        while k < l and v_k == nums[k]:
                            k += 1
                        while k < l and v_l == nums[l]:
                            l -= 1


# leetcode submit region end(Prohibit modification and deletion)

s = Solution.fourSum(None, nums=[1, 0, -1, 0, -2, 2], target=0)
s = Solution.fourSum(None, nums=[-2, -1, -1, 1, 1, 2, 2], target=0)
print(list(s))

# Success:
# Runtime: 980 ms, faster than 46.40% of Python3 online submissions.
# Memory Usage: 14.1 MB, less than 92.81% of Python3 online submissions.
