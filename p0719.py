def smallestDistancePair(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    import heapq
    from itertools import combinations
    h = []
    for pair in combinations(nums, 2):
        heapq.heappush(h, abs(pair[1] - pair[0]))
    return heapq.nsmallest(k, h)[-1]


print(smallestDistancePair([1, 6, 1], 3))
print(smallestDistancePair([1, 3, 1], 1))