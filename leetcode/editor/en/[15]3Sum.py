# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k
# ]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
#  Notice that the solution set must not contain duplicate triplets.
#
#
#  Example 1:
#  Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
#  Example 2:
#  Input: nums = []
# Output: []
#  Example 3:
#  Input: nums = [0]
# Output: []
#
#
#  Constraints:
#
#
#  0 <= nums.length <= 3000
#  -105 <= nums[i] <= 105
#
#  Related Topics Array Two Pointers Sorting
#  👍 11593 👎 1149

from typing import List
import collections
from bisect import bisect_left


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        counter = collections.defaultdict(int)
        for i in nums:
            counter[i] += 1

        nums = sorted(counter)
        if nums[0] > 0 or nums[-1] < 0:
            return []

        output = []
        # find answer with no duplicates within combo
        for i in range(len(nums)):
            # search range
            twoSum = -nums[i]
            min_half, max_half = twoSum - nums[-1], twoSum / 2
            l = bisect_left(nums, min_half, i + 1)
            r = bisect_left(nums, max_half, l)

            for j in nums[l:r]:
                if twoSum - j in counter:
                    output.append([nums[i], j, twoSum - j])

        # find ans with duplicates within combo
        for k in counter:
            if counter[k] > 1:
                if k == 0 and counter[k] >= 3:
                    output.append([0, 0, 0])
                elif k != 0 and -2 * k in counter:
                    output.append([k, k, -2 * k])
        return output


# leetcode submit region end(Prohibit modification and deletion)

s = Solution.threeSum(None, [0, 0, 0])
print(list(s))

# Success:
# Runtime: 332 ms, faster than 99.07% of Python3 online submissions. \
# Memory Usage: 18.2 MB, less than 17.86% of Python3 online submissions.

# Success:
# Runtime: 6332 ms, faster than 6.69% of python3 online submissions.
# Memory Usage: 17.6 MB, less than 38.81% of Python3 online submissions.

# def threeSum(self, nums: List[int]) -> List[List[int]]:
#     if len(nums) < 3:
#         return []
#
#     d = {}
#     s = set()
#     for i, n in enumerate(nums):
#         d[n] = d.get(n, 0) + 1
#
#     out = []
#     for i, n1 in enumerate(nums[:-1]):
#         for j, n2 in enumerate(nums[i + 1:]):
#             half_t = (n1, n2) if n1 < n2 else (n2, n1)
#             sum = -1 * (n1 + n2)
#             if sum in d:
#                 # No unique k
#                 if ((n1 == sum) + (n2 == sum)) >= d[sum]:
#                     continue
#
#                 # Tuple to lookup
#                 if sum < half_t[0]:
#                     tup = (sum, *half_t)
#                 elif sum < half_t[1]:
#                     tup = (half_t[0], sum, half_t[1])
#                 else:
#                     tup = (*half_t, sum)
#
#                 if tup not in s:
#                     s.add(tup)
#                     out.append(tup)
#     return out

# Runtime: 804 ms, faster than 78.73 % of
# Memory Usage: 16 MB, less than 99.92 % of

# nums.sort()
# last_v_i = None
#
# for i in range(len(nums)):
#     # Goal of the sum
#     v_i = -nums[i]
#     # Repeats of i
#     if last_v_i == v_i:
#         continue
#
#     last_v_i = v_i
#
#     j = i + 1
#     k = len(nums) - 1
#
#     while j < k:
#         v_j = nums[j]
#         v_k = nums[k]
#
#         # Increase j because sum will increase
#         if (v_j + v_k) < v_i:
#             j += 1
#         # Increase k because sum will decrease
#         elif (v_j + v_k) > v_i:
#             k -= 1
#         else:
#             yield (nums[i], v_j, v_k)
#
#             # Duplicates in j
#             while j < k and nums[j] == v_j:
#                 j += 1
#
#             # Duplicates in k
#             while j < k and nums[k] == v_k:
#                 k -= 1
