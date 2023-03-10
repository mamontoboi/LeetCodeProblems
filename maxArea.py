def maxArea(height: list):
    """
    :type height: List[int]
    :rtype: int
    """
    result = 0
    l, r = 0, len(height) - 1

    while r > l:
        area = (r - l) * min(height[l], height[r])
        result = max(area, result)

        if height[l] < height[r]:
            l += 1

        else:
            r -= 1

    return result


print(maxArea([1,8,6,2,5,4,8,3,7]))

