def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    from itertools import combinations
    d = {key: 0 for key in nums}
    print(d)
    total = []

    for i, j in combinations(nums, 2):
        print(i,j,d.get(-1*(i + j), False))
        if d.get(-1*(i + j), False):
            print(i, j, -1*(i+j))
            total.append(( i, j, -1*(i+j) ))
    return total


print(threeSum([-1, 0, 1, 2, -1, -4]))
