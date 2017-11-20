from timeit import Timer


def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """

    low, high = 0, len(height) - 1
    largest = min(height[low], height[high]) * (high - low)
    for _ in range(len(height)-2):
        if height[low] > height[high]:
            high -= 1
        else:
            low += 1
        largest = max(largest, min(height[low], height[high])*(high - low))
    return largest


maxArea([1, 3, 6, 4, 2, 5])
# t = Timer(lambda: maxArea([1, 3, 6, 4, 2, 5]))
# print(t.timeit(number=1000))
