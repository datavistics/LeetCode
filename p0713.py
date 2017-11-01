def numSubarrayProductLessThanK(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """

    # import sys
    # sys.setcheckinterval(100000)
    running_prod, first_ind, total = 1, 0, 0
    l = len(nums)

    for i,v in enumerate(nums):
        running_prod *= v
        if running_prod >= k:
            while first_ind < l and running_prod >= k:
                running_prod /= nums[first_ind]
                first_ind += 1
        if v < k:
            total += i - first_ind + 1
        else:
            running_prod = 1
            first_ind = 1 + i
        print(running_prod, total)
    return total

print(numSubarrayProductLessThanK(nums = [10,9,10,4,3,8,3,3,6,2,10,10,9,3], k = 19))